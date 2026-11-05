
from app.services.github_pr_service import get_pull_request_files


owner = "s-sandhiya-06"
repo = "reviewx-ai-code-reviewer"
pr_number = 1

try:
    files = get_pull_request_files(owner, repo, pr_number)

    print("\nPull Request files fetched successfully!")
    print("Total changed files:", len(files))

    for file in files:
        print("\nFilename:", file["filename"])
        print("Status:", file["status"])
        print("Additions:", file["additions"])
        print("Deletions:", file["deletions"])
        print("Changes:", file["changes"])
        print("Patch available:", file["patch"] is not None)

except Exception as e:
    print("Error:", e)
