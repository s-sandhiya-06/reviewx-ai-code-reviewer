
import hashlib
import hmac

from fastapi import APIRouter, Request, HTTPException
from app.core.config import settings

router = APIRouter(
    prefix="/webhooks",
    tags=["GitHub Webhooks"]
)


def verify_signature(payload: bytes, signature: str):
    if not signature:
        return False

    expected_signature = "sha256=" + hmac.new(
        settings.GITHUB_WEBHOOK_SECRET.encode("utf-8"),
        payload,
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(
        expected_signature,
        signature
    )


@router.post("/github")
async def github_webhook(request: Request):

    # Read the original request body
    payload = await request.body()

    # Get GitHub signature
    signature = request.headers.get(
        "X-Hub-Signature-256", ""
    )

    # Verify webhook authenticity
    if not verify_signature(payload, signature):
        raise HTTPException(
            status_code=401,
            detail="Invalid webhook signature"
        )

    event = request.headers.get("X-GitHub-Event")

    if event == "pull_request":
        data = await request.json()

        action = data.get("action")
        repository = data.get("repository", {}).get("full_name")
        pr_number = data.get("number")

        print("Pull Request Event Received!")
        print("Action:", action)
        print("Repository:", repository)
        print("PR Number:", pr_number)

        return {
            "message": "Pull request event received",
            "action": action,
            "repository": repository,
            "pull_request_number": pr_number
        }

    return {
        "message": "Webhook received",
        "event": event
    }
