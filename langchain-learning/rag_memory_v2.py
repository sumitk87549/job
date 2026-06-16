from dotenv import load_dotenv

load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from langchain.chains import (create_history_aware_retriever, create_retrieval_chain)
from langchain.chains.combine_documents import create_stuff_documents_chain

document = PyPDFLoader("./books/AOSH.pdf").load()

doc_splitted = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=60).split_documents(document)

embedding_obj = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = Chroma.from_documents(doc_splitted, embedding_obj)
model = ChatGroq(model="llama-3.1-8b-instant")
chat_memory = []
retr = vector_store.as_retriever(search_kwargs={"k":3})
flow = True
while flow:
    que = input("ask me:\n")
    if que.lower() == 'exit':
        break

    retrieved_chunks = retr.invoke(que)
    context = '\n'.join([a.page_content for a in retrieved_chunks])

    prompt = ChatPromptTemplate.from_template(f"Answer QUESTION based Only on Given CONTEXT and CHAT_HISTORY [return only anwer the questoin without commentary] \n\nCONTEXT:\n {context} \n\nCHAT_HISTORY:\n {chat_memory} \n\nQUESTION:\n{que}")
    parser = StrOutputParser()

    chain = prompt | model | parser

    res = chain.invoke({
        "context": context,
        "que": que,
        "chat_memory": chat_memory,
    })
    print(res)

    chat_memory.append(['User: ',que,'\nAI: ',res])
