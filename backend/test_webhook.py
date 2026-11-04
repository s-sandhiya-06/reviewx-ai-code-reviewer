
import hashlib
import hmac
import json

from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings

client = TestClient(app)

payload = {
    "action": "opened",
    "number": 1,
    "repository": {
        "full_name": "s-sandhiya-06/reviewx-ai-code-reviewer"
    }
}

body = json.dumps(payload).encode("utf-8")

# Generate a valid GitHub-style signature
signature = "sha256=" + hmac.new(
    settings.GITHUB_WEBHOOK_SECRET.encode("utf-8"),
    body,
    hashlib.sha256
).hexdigest()

headers = {
    "X-GitHub-Event": "pull_request",
    "X-Hub-Signature-256": signature
}

# Test valid signature
response = client.post(
    "/webhooks/github",
    content=body,
    headers=headers
)

print("Valid signature status:", response.status_code)
print("Valid signature accepted:", response.status_code == 200)

# Test invalid signature
headers["X-Hub-Signature-256"] = "sha256=invalid"

response = client.post(
    "/webhooks/github",
    content=body,
    headers=headers
)

print("Invalid signature status:", response.status_code)
print("Invalid signature rejected:", response.status_code == 401)
