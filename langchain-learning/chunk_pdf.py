from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

def generate_chunks(pdf_path):
    loader = PyPDFLoader(pdf_path)
    doc = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=70)
    chunks = splitter.split_documents(doc)
    print("Number of chunks: " + str(len(chunks)))
    return chunks

# loader = PyPDFLoader("./books/AOSH.pdf")

# doc = loader.load()

# splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

# chunks = splitter.split_documents(doc)

# print("\n\n*****LENGTH CHUNKS*****\n")
# print(len(chunks))

# print("\n\n*****Chunked DATA*****\n")
# print(chunks[3].page_content)

# print("\n\n*****METADATA*****\n")
# print(chunks[3].metadata)