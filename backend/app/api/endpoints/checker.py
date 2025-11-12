from fastapi import APIRouter
from app.schemas.checker import CheckRequest

router = APIRouter()

@router.post("/check-url")
def check_url(request: CheckRequest):
    # For now, we just receive the URL and send a dummy response back.
    # Later, this is where you'll call your nlp_service and web_service.
    print(f"Received URL for checking: {request.url}")

    return {
        "status": "received",
        "url_checked": request.url,
        "is_true": False,
        "truth_percentage": 15.5,
        "justification": "This is a dummy response from the server."
    }