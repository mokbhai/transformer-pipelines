from fastapi import APIRouter
from models.types import MaskedLanguageModelingRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def fill_mask(request: MaskedLanguageModelingRequest):
    # TODO: Implement masked language modeling
    return PipelineResult(success=True, data={"predictions": "Not implemented yet"})