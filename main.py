from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Allow requests from your frontend
origins = [
    "http://localhost:5173",  # Vite/Vue dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------
# Data Models
# ------------------------

class Rule(BaseModel):
    fieldName: str
    expression: str
    successEvent: str
    errorMessage: str
    enabled: bool

class RuleRequest(BaseModel):
    WorkflowName: str
    Rules: List[Rule]

# ------------------------
# API Endpoint
# ------------------------

@app.post("/api/rules")
async def receive_rules(data: RuleRequest):
    print("Received Rules for Workflow:", data.WorkflowName)
    for rule in data.Rules:
        print(rule)
    return {"message": "Rules saved successfully", "total": len(data.Rules)}

# Optional test endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}

# ------------------------
# Run the server
# ------------------------

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
