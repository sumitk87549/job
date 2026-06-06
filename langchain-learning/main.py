from dotenv import load_dotenv
from langchain_core import prompts
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model = 'llama-3.1-8b-instant')
parser = StrOutputParser()
langf = input("From Language: ")
langt = input("To Language: ")
text = input("Enter text:\n ")
prompt = ChatPromptTemplate.from_template("translate the text from {langf} into {langt} [GIVE TRANSLATED TEXT ONLY]: \n \"\"\"{text}\"\"\"")
chain = prompt | model | parser

print("Translated text:\n",chain.invoke({"langf":langf , "langt":langt , "text":text}))
