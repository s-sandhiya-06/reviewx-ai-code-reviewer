
from app.core.github_client import get_repository_info

try:
    repo = get_repository_info()

    print("Repository access successful!")
    print("Repository:", repo["full_name"])
    print("Private:", repo["private"])
    print("Default branch:", repo["default_branch"])

except Exception as e:
    print("Repository access failed:", str(e))
