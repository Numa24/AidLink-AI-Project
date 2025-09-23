from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn 
from ai.recommender import match_volunteer


app = FastAPI()

class NGORequest(BaseModel):
    description: str

@app.get("/")
def home():
    return {"message": "Welcome to AidLink Backend 🚀"}

@app.post("/match")
def match(request: NGORequest):
    result = match_volunteer(request.description)
    return {"recommendation": result}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

