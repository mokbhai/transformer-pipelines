from fastapi import APIRouter
from models.types import ImageClassificationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def classify_image(request: ImageClassificationRequest):
    # TODO: Implement image classification
    return PipelineResult(success=True, data={"classes": "Not implemented yet"})