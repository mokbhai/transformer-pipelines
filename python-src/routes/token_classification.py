from fastapi import APIRouter
from models.types import TokenClassificationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def classify_tokens(request: TokenClassificationRequest):
    # TODO: Implement token classification
    return PipelineResult(success=True, data={"tokens": "Not implemented yet"})