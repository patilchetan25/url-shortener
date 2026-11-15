# The HTTP side of the URL shortener: reading requests and sending responses.
# The actual logic lives in the service. These functions only translate between HTTP and it.
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from app.config import BASE_URL
from app.models.url import ShortenRequest, ShortenResponse
from app.services.url_service import get_long_url, shorten_url

router = APIRouter()


@router.post("/shorten", response_model=ShortenResponse)
def shorten(request: ShortenRequest) -> ShortenResponse:
    # Hand the URL to the service as plain text, and get a free code back.
    code = shorten_url(str(request.url))
    # Building the full link is about how the API presents itself, so it stays here.
    return ShortenResponse(code=code, short_url=f"{BASE_URL}/{code}")


# Catches any single path segment, so main.py must include this router last.
@router.get("/{code}")
def redirect(code: str) -> RedirectResponse:
    long_url = get_long_url(code)
    # The service says "not found" with None. The route turns that into an HTTP 404.
    if long_url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=long_url, status_code=302)