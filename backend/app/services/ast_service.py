import ast
from pathlib import Path


class CodeAnalyzer(ast.NodeVisitor):

    def __init__(self, filename):
        self.filename = filename
        self.findings = []

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            if node.func.id in ["eval", "exec"]:
                self.findings.append({
                    "rule_id": "AST001",
                    "file": self.filename,
                    "severity": "HIGH",
                    "message": f"Use of {node.func.id}() can be unsafe",
                    "line": node.lineno
                })

        self.generic_visit(node)

    def visit_ExceptHandler(self, node):
        if node.type is None:
            self.findings.append({
                "rule_id": "AST002",
                "file": self.filename,
                "severity": "LOW",
                "message": "Bare except block detected",
                "line": node.lineno
            })

        self.generic_visit(node)


def run_ast_analysis(target_path):

    path = Path(target_path)

    files = [path] if path.is_file() else list(path.rglob("*.py"))

    all_findings = []
    errors = []

    for file in files:
        try:
            source = file.read_text(encoding="utf-8")
            tree = ast.parse(source)

            analyzer = CodeAnalyzer(str(file))
            analyzer.visit(tree)

            all_findings.extend(analyzer.findings)

        except (SyntaxError, UnicodeDecodeError) as e:
            errors.append({
                "file": str(file),
                "error": str(e)
            })

    return {
        "total_findings": len(all_findings),
        "findings": all_findings,
        "errors": errors
    }