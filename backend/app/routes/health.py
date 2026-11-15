from fastapi import APIRouter
# A router is a mini-app holding a group of routes. main.py plugs it into the real app.
router = APIRouter()

# @router.get instead of @app.get: this route belongs to the router for now.
@router.get("/health")
def health():
    return {"status": "ok"}