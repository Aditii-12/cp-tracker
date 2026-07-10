from fastapi import APIRouter, HTTPException
from backend.services.run_analysis import generate_full_report

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.get("/{handle}")
def analyze_handle(handle: str):
    try:
        report = generate_full_report(handle)
        return report
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
