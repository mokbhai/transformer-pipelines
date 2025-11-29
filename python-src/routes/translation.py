from fastapi import APIRouter
from models.types import TranslationRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def translate(request: TranslationRequest):
    # TODO: Implement translation
    return PipelineResult(success=True, data={"translation": "Not implemented yet"})