from fastapi import APIRouter
from models.types import OcrRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def perform_ocr(request: OcrRequest):
    # TODO: Implement OCR
    return PipelineResult(success=True, data={"text": "Not implemented yet"})