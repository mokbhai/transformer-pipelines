from fastapi import APIRouter
from models.types import TextGenerationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def generate_text(request: TextGenerationRequest):
    # TODO: Implement text generation
    return PipelineResult(success=True, data={"generated_text": "Not implemented yet"})