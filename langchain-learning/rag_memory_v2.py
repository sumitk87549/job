from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

document = PyPDFLoader("./books/AOSH.pdf").load()
hf_embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


split_chunks = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(document)
vectors = Chroma.from_documents(documents=split_chunks, embedding=hf_embedding)

retriever = vectors.as_retriever(search_kwargs={"k":3,})
parser = StrOutputParser()
model = ChatGroq(model='llama-3.1-8b-instant')

chat_history=[]

while True:
    que = input("Ask me: ")
    chunks = retriever.invoke(que)

    if que.lower() == 'exit':
        break

    context = '\n\n'.join([chk.page_content for chk in chunks])
    prompt = ChatPromptTemplate.from_template("Answer question based only on the CONTEXT [Give Answer Only]\n\nCONTEXT:{context}\n\nQUESTION:{question}\n\nCHAT_HISTORY:{chat_history}")
    chain = prompt | model | parser
    res = chain.invoke({
        "context": context,
        "question": que,
        "chat_history": chat_history
    })

    print("RESPONSE:\\n\n",res)

    chat_history.append(f"User: {que}\nAI: {res}")