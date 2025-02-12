import math
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List
from pydantic import BaseModel
import os

app = FastAPI(title="FastAPI Server", version="1.0.0")

class AddRequest(BaseModel):
    a: float
    b: float

class MultiplyRequest(BaseModel):
    a: float
    b: float

class DivideRequest(BaseModel):
    a: float
    b: float

class Calculator:
    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        return a / b

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

@app.post("/multiply")
async def multiply_numbers(request: MultiplyRequest) -> Dict[str, float]:
    """Multiply two numbers"""
    calculator = Calculator()
    result = calculator.multiply(request.a, request.b)
    return {"result": result}

@app.post("/divide")
async def divide_numbers(request: DivideRequest) -> Dict[str, float]:
    """Divide two numbers"""
    calculator = Calculator()
    result = calculator.divide(request.a, request.b)
    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
