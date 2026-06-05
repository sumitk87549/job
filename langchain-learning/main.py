from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = 'llama-3.1-8b-instant')
cntry = input("Enter Country for which you want to know capital: ")
prompt = ChatPromptTemplate.from_template("what is the capital of {country}")
parser = StrOutputParser()
chain = prompt | model | parser

response = chain.invoke({ "country": cntry })
print("The Capital of "+cntry+" is",response)