# agent.py

from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from tools import WebSearchTool, FileWriterTool

# Use the key from .env
llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0)

tools = [
   Tool.from_function(WebSearchTool()._run, name="WebSearch", description="Searches web"),
Tool.from_function(FileWriterTool()._run, name="FileWriter", description="Writes to file"),
]

agent_executor = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

