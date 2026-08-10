from dotenv import load_dotenv
import os
import logging
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from pydantic import BaseModel, Field
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
#from langchain_core. import TavilySearch
class SearchInput(BaseModel):
    a: int = Field(..., description="The first number to add.")
    b: int = Field(..., description="The second number to add.")

class SearchOutput(BaseModel):
    total: int = Field(..., description="The sum of the two numbers.")

logging.basicConfig(level=logging.INFO)
logging.info("Loading environment variables...")
load_dotenv()  # take environment variables from .env.

@tool(description="Adds two numbers", args_schema=SearchInput)
def add_numbers(a: int, b: int) -> int:
    """
    This tool takes two numbers as input and returns their sum. It is designed to be used in a LangChain agent for performing addition operations.
    """
    return a+b

def subtract_numbers(a: int, b: int) -> int:
    """
    This tool takes two numbers as input and returns their difference. It is designed to be used in a LangChain agent for performing subtraction operations.
    """
    return a-b

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm=init_chat_model("openai:gpt-5.4-mini", temperature=0)
agent=create_agent(model=llm, tools=[add_numbers, subtract_numbers],response_format=SearchOutput)
def main():
    if OPENAI_API_KEY is None:
        logging.info("OPENAI_API_KEY is not set in the environment variables.")
    print("Hello from langchain-course!")
    prompt = ChatPromptTemplate.from_messages(
            messages=[
                {"role": "system", "content": "You are a helpful assistant capable of  performing calculations and provide informative responses using the tools available."}, 
                {"role": "user", "content": "{question}"}
            ]
        )
    chain = prompt | agent
    agent_response=chain.invoke({"question":"What is the sum of 10.12 and 23.45 and subtract the result from 50?"})
    logging.info(f"Chat Prompt Template Result: {prompt}")
    logging.info(f"Agent Response: {type(agent_response.get("messages"))}")
    if agent_response.get("messages"):
        logging.info(f"Agent Response Messages: {agent_response.get("messages")}")
    logging.info(f"Agent Response Messages: {agent_response["structured_response"]}")


if __name__ == "__main__":
    main()
    