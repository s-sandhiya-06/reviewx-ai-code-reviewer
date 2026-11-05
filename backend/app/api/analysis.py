from pathlib import Path

from fastapi import APIRouter, HTTPException
from app.services.static_analysis_service import run_static_analysis

router = APIRouter(prefix="/analysis", tags=["Static Analysis"])


@router.post("/scan")
def scan_application():

    target_path = Path(__file__).resolve().parents[1]

    try:
        report = run_static_analysis(str(target_path))
        return report

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Static analysis failed"
        )