
import httpx

from app.core.github_auth import create_github_jwt

GITHUB_API = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_installation_access_token():
    jwt_token = create_github_jwt()

    headers = {
        **HEADERS,
        "Authorization": f"Bearer {jwt_token}"
    }

    response = httpx.get(
        f"{GITHUB_API}/app/installations",
        headers=headers,
        timeout=15
    )
    response.raise_for_status()

    installations = response.json()

    installation = next(
        (
            item for item in installations
            if item["account"]["login"] == "s-sandhiya-06"
        ),
        None
    )

    if not installation:
        raise Exception("ReviewX GitHub App installation not found")

    installation_id = installation["id"]

    token_response = httpx.post(
        f"{GITHUB_API}/app/installations/{installation_id}/access_tokens",
        headers=headers,
        timeout=15
    )
    token_response.raise_for_status()

    return token_response.json()["token"]


def get_repository_info():
    token = get_installation_access_token()

    headers = {
        **HEADERS,
        "Authorization": f"Bearer {token}"
    }

    response = httpx.get(
        f"{GITHUB_API}/repos/s-sandhiya-06/reviewx-ai-code-reviewer",
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return response.json()
