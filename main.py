from fastapi import FastAPI, Request
from pydantic import BaseModel
from agent import agent_executor
from pubsub import publish_message

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run-agent/")
def run_agent(req: TaskRequest):
    try:
        result = agent_executor.run(req.task)
        publish_message("agent-log", f"Task: {req.task} → Result: {result}")
        return {"output": result}
    except Exception as e:
        # Print the actual error in the server
        print("❌ Error while running agent:", e)
        return {"error": str(e)}

