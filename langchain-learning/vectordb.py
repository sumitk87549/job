from langchain_community.vectorstores import Chroma
from chunk_pdf import generate_chunks
from langchain_huggingface import HuggingFaceEmbeddings

chunks = generate_chunks("./books/AOSH.pdf")

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# vecstore = Chroma.from_documments(document=chunks, embedding=embeddings)
