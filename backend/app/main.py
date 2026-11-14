from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
import secrets
import string

class ShortenRequest(BaseModel):
    url: HttpUrl

class ShortenResponse(BaseModel):
    code: str
    short_url: HttpUrl

ALPHABET = string.ascii_letters + string.digits
CODE_LENGTH = 7

def generate_code() -> str:
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))






app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

def generate_code() -> str:
    code = ""                                 # Start with an empty string
    for _ in range(CODE_LENGTH):              # Repeat 7 times
        code = code + secrets.choice(ALPHABET)  # Add one random character
    return code                               # e.g. "aB3xK9q"
