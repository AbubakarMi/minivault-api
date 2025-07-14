from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os, json

app = FastAPI()

# Ensure log directory exists
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.jsonl")
os.makedirs(LOG_DIR, exist_ok=True)

# Input model
class PromptRequest(BaseModel):
    prompt: str

# Output model
class ResponseModel(BaseModel):
    response: str

# POST /generate endpoint
@app.post("/generate", response_model=ResponseModel)
async def generate_response(data: PromptRequest):
    prompt = data.prompt
    response = f"This is a stubbed response to: {prompt}"

    # Save to log file
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "prompt": prompt,
        "response": response
    }

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

    return {"response": response}
