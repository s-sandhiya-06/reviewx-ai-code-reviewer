from app.services.static_analysis_service import run_static_analysis

report = run_static_analysis("app")

print("\nStatic Analysis completed!")
print("Total findings:", report["total_findings"])

for finding in report["findings"]:
    print("\nSource:", finding["source"])
    print("Rule:", finding["rule_id"])
    print("File:", finding["file"])
    print("Severity:", finding["severity"])
    print("Message:", finding["message"])
    print("Line:", finding["line"])

print("\nSemgrep errors:", len(report["semgrep_errors"]))
print("AST errors:", len(report["ast_errors"]))