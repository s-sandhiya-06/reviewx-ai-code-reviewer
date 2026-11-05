from app.services.semgrep_service import run_semgrep
from app.services.ast_service import run_ast_analysis


def normalize_severity(severity):

    severity = severity.upper()

    if severity in ["ERROR", "CRITICAL", "HIGH"]:
        return "HIGH"

    if severity in ["WARNING", "MEDIUM"]:
        return "MEDIUM"

    return "LOW"


def run_static_analysis(target_path: str):

    semgrep_report = run_semgrep(target_path)
    ast_report = run_ast_analysis(target_path)

    findings = []
    seen_findings = set()

    # Process Semgrep findings
    for finding in semgrep_report["findings"]:

        item = {
            "source": "Semgrep",
            "rule_id": finding["check_id"],
            "file": finding["path"],
            "severity": normalize_severity(
                finding["extra"]["severity"]
            ),
            "message": finding["extra"]["message"],
            "line": finding["start"]["line"]
        }

        key = (item["file"], item["line"], item["message"])

        if key not in seen_findings:
            findings.append(item)
            seen_findings.add(key)

    # Process AST findings
    for finding in ast_report["findings"]:

        item = {
            "source": "Python AST",
            "rule_id": finding["rule_id"],
            "file": finding["file"],
            "severity": normalize_severity(finding["severity"]),
            "message": finding["message"],
            "line": finding["line"]
        }

        key = (item["file"], item["line"], item["message"])

        if key not in seen_findings:
            findings.append(item)
            seen_findings.add(key)

    return {
        "total_findings": len(findings),
        "findings": findings,
        "semgrep_errors": semgrep_report["errors"],
        "ast_errors": ast_report["errors"]
    }