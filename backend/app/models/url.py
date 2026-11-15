# The shapes of data going in and out of the URL endpoints.
# This file only describes data: it has no logic and no HTTP.
from pydantic import BaseModel, HttpUrl


# What the client sends to POST /shorten.
class ShortenRequest(BaseModel):
    url: HttpUrl


# What POST /shorten sends back.
class ShortenResponse(BaseModel):
    code: str
    short_url: HttpUrl
