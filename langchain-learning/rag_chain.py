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

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
print("embeddings created\n")
vectors = Chroma.from_documents(documents=book, embedding=embeddings)
print("Vectors created\n")

splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=60)
retiever = vectors.as_retriever(search_kwargs={"k":3})
print("Vectors retrieved\n")
prompt=ChatPromptTemplate.from_template("Answer the question based on the following context [GIVE ANSWER ONLY]: \n {context} \n Question: {question}")
print("Prompt created\n")

parser = StrOutputParser()
model = ChatGroq(model='llama-3.1-8b-instant')
question = input("ask me : ")
chain = prompt | model | parser 


# ***********NEW***********
retrieved_docs = retiever.invoke(question)
context = '\n\n'.join([doc.page_content for doc in retrieved_docs])
response = chain.invoke({"context": context, "question": question})
print("\nLLM working...\n")

print("\n\nAnswer:\n",response)
