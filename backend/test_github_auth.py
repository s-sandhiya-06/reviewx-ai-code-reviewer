
import jwt
from app.core.github_auth import create_github_jwt

token = create_github_jwt()

print("JWT generated successfully!")
print("Token has 3 parts:", len(token.split(".")) == 3)

# Inspect claims without verifying the signature
payload = jwt.decode(
    token,
    options={"verify_signature": False}
)

print("App ID:", payload["iss"])
print("JWT algorithm: RS256")
