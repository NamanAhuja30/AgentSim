# tools.py
from langchain.tools import BaseTool
from typing import Optional, Type

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for information"

    def _run(self, query: str):
        # Replace with real search logic
        return f"Search result for: {query}"

    def _arun(self, query: str):
        raise NotImplementedError("Async not implemented")

class FileWriterTool(BaseTool):
    name: str = "file_writer"
    description: str = "Write text to a file"

    def _run(self, content: str):
        with open("agent_output.txt", "w") as f:
            f.write(content)
        return "Content written to file"

    def _arun(self, content: str):
        raise NotImplementedError("Async not implemented")

