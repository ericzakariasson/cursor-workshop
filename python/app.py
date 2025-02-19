import math
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from pydantic import BaseModel
import os
import boto3
from botocore.exceptions import ClientError

app = FastAPI(title="FastAPI Server", version="1.0.0")

class AddRequest(BaseModel):
    a: float
    b: float

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/add")
async def add_numbers(request: AddRequest) -> Dict[str, float]:
    """Add two numbers"""
    calculator = Calculator()
    result = calculator.add(request.a, request.b)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
