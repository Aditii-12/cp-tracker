from fastapi import APIRouter, HTTPException
from backend.services.run_analysis import generate_full_report
from backend.services.analysis.weak_topic_analysis import get_weak_topics
from backend.services.recommender.suggest import recommend_problems
from backend.services.api.codeforces import get_rating_history

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.get("/{handle}")
def analyze_handle(handle: str):
    try:
        report = generate_full_report(handle)
        return report
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{handle}/recommendations")
def recommendations(handle: str):
    try:
        weak_topics = get_weak_topics(handle)
        return recommend_problems(handle, weak_topics)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{handle}/rating-history")
def rating_history(handle: str):
    try:
        history = get_rating_history(handle)
        return [
            {
                "contest": h["contestName"],
                "date": h["ratingUpdateTimeSeconds"],
                "rating": h["newRating"],
                "change": h["newRating"] - h["oldRating"],
            }
            for h in history
        ]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
