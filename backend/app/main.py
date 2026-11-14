from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

class ShortenRequest(BaseModel):
    url: HttpUrl

class ShortenResponse(BaseModel):
    short_url: HttpUrl






app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}