from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from fastapi.responses import RedirectResponse

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

BASE_URL = "http://localhost:8000"
urls: dict[str, str] = {}



app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/shorten", response_model=ShortenResponse)
def shorten(request: ShortenRequest) -> ShortenResponse:
    code = generate_code()
    while code in urls:
        code = generate_code()
    

    urls[code] = str(request.url)
    short_url = f"{BASE_URL}/{code}"
    return ShortenResponse(code=code, short_url=short_url)

@app.get("/{code}")
def redirect(code: str) -> RedirectResponse: 
    long_url = urls.get(code)
    if long_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=long_url, status_code=302)

