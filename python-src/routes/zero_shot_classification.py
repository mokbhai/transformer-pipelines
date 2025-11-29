from fastapi import APIRouter
from models.types import ZeroShotClassificationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def classify_zero_shot(request: ZeroShotClassificationRequest):
    # TODO: Implement zero-shot classification
    return PipelineResult(success=True, data={"classes": "Not implemented yet"})