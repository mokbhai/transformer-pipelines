from fastapi import APIRouter
from models.types import ObjectDetectionRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def detect_objects(request: ObjectDetectionRequest):
    # TODO: Implement object detection
    return PipelineResult(success=True, data={"objects": "Not implemented yet"})