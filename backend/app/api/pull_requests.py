
from fastapi import APIRouter, HTTPException
import httpx

from app.services.github_pr_service import get_pull_request_files


router = APIRouter(
    prefix="/pull-requests",
    tags=["Pull Requests"]
)


@router.get("/{owner}/{repo}/{pr_number}/files")
def fetch_pr_files(owner: str, repo: str, pr_number: int):

    try:
        files = get_pull_request_files(owner, repo, pr_number)

        return {
            "repository": f"{owner}/{repo}",
            "pull_request_number": pr_number,
            "total_files": len(files),
            "files": files
        }

    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail="GitHub API request failed"
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to connect to GitHub"
        )
