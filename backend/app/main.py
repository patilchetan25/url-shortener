# The entry point: create the app and plug in each group of routes.
# Uvicorn still finds it through "app.main:app".
from fastapi import FastAPI

from app.routes import health, urls

app = FastAPI()

# Order matters. FastAPI checks routes in the order they're added, and urls has
# the catch-all GET /{code}. Adding health first keeps /health from being treated as a code.
app.include_router(health.router)
app.include_router(urls.router)