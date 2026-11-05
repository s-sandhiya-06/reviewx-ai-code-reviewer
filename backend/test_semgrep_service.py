
from app.services.semgrep_service import run_semgrep

try:
    report = run_semgrep("app")

    print("\nSemgrep scan completed!")
    print("Total findings:", report["total_findings"])

    for finding in report["findings"]:
        print("\nRule ID:", finding["check_id"])
        print("File:", finding["path"])
        print("Severity:", finding["extra"]["severity"])
        print("Message:", finding["extra"]["message"])
        print("Line:", finding["start"]["line"])

    print("\nSemgrep errors:", len(report["errors"]))

except Exception as e:
    print("Scan failed:", str(e))
