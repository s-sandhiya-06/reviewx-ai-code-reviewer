
import time
import jwt

from pathlib import Path
from app.core.config import settings


def create_github_jwt():
    # Read the private key
    private_key_path = Path(settings.GITHUB_PRIVATE_KEY_PATH)

    with open(private_key_path, "r") as key_file:
        private_key = key_file.read()

    # JWT payload
    now = int(time.time())

    payload = {
        "iat": now - 60,
        "exp": now + (9 * 60),
        "iss": str(settings.GITHUB_APP_ID)
    }

    # Sign JWT using RS256
    token = jwt.encode(
        payload,
        private_key,
        algorithm="RS256"
    )

    return token
