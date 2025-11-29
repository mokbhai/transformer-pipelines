from fastapi import APIRouter
from models.types import SentimentAnalysisRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def analyze_sentiment(request: SentimentAnalysisRequest):
    # TODO: Implement sentiment analysis
    return PipelineResult(success=True, data={"sentiment": "Not implemented yet"})