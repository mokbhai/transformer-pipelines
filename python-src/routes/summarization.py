from fastapi import APIRouter
from models.types import SummarizationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def summarize_text(request: SummarizationRequest):
    # TODO: Implement summarization
    return PipelineResult(success=True, data={"summary": "Not implemented yet"})