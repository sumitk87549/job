from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

book = PyPDFLoader("./books/AOSH.pdf").load()

embedding_object = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("embeddings created")

split_chunks = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=60).split_documents(book)
vectors = Chroma.from_documents(documents=split_chunks, embedding=embedding_object)
print("Vectors created")
retriever = vectors.as_retriever(seach_kwargs={"k":5})
model = ChatGroq(model='llama-3.1-8b-instant')
parser = StrOutputParser()
chat_memory = []

while True:
    que = input("Ask me: ")
    retrieved_chunks = retriever.invoke(que)

    if que.lower() == 'exit':
        print("Exiting...")
        break

    context = '\n\n'.join([chk.page_content for chk in retrieved_chunks])
    prompt = ChatPromptTemplate.from_template("Answer the question based only on the following context [Give Answer only] \n\n CHAT_HISTORY: {chat_memory} \n\n CONTEXT: {context} \n\n QUESTION: {question}")
    chain = prompt | model | parser
    res = chain.invoke({
        "chat_memory": chat_memory,
        "context": context,
        "question": que
    })
    print("\nLLM working...\n")
    print("\nAnswer:\n", res, "\n\n")
    chat_memory.append(f"User: {que}\nAI:{res}")
    