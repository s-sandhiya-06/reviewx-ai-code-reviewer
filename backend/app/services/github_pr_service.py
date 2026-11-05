
import httpx

from app.core.github_client import get_installation_access_token


GITHUB_API = "https://api.github.com"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}


def get_pull_request_files(owner: str, repo: str, pr_number: int):

    token = get_installation_access_token()

    headers = {
        **HEADERS,
        "Authorization": f"Bearer {token}"
    }

    files = []
    page = 1

    while True:
        response = httpx.get(
            f"{GITHUB_API}/repos/{owner}/{repo}/pulls/{pr_number}/files",
            headers=headers,
            params={
                "per_page": 100,
                "page": page
            },
            timeout=30
        )

        response.raise_for_status()

        page_files = response.json()

        if not page_files:
            break

        for file in page_files:
            files.append({
                "filename": file["filename"],
                "status": file["status"],
                "additions": file["additions"],
                "deletions": file["deletions"],
                "changes": file["changes"],
                "patch": file.get("patch")
            })

        page += 1

    return files
