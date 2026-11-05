
import json
import subprocess


def run_semgrep(target_path: str):

    command = [
        "semgrep",
        "scan",
        "--config", "auto",
        "--json",
        target_path
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=300
    )

    if not result.stdout:
        raise RuntimeError(
            f"Semgrep failed: {result.stderr}"
        )

    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            "Unable to parse Semgrep JSON output"
        ) from e

    return {
        "total_findings": len(report.get("results", [])),
        "findings": report.get("results", []),
        "errors": report.get("errors", [])
    }
