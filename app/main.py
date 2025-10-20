from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ChatGPT Action Demo", version="1.0.0")

class GreetRequest(BaseModel):
    name: str

class GreetResponse(BaseModel):
    message: str

API_KEY_ENV = "demo-secret-key"  # swap for something safer in production

@app.post("/greet", response_model=GreetResponse, summary="Say hi")
def greet(req: GreetRequest, x_api_key: str | None = Header(None)):
    # Simple API key check for the demo
    if x_api_key != API_KEY_ENV:
        raise HTTPException(status_code=401, detail="Invalid or missing X-API-Key")
    return GreetResponse(message=f"Hello, {req.name}! 👋")
    