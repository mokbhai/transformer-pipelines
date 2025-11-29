from fastapi import APIRouter
from models.types import QuestionAnsweringRequest, PipelineResult
from utils.pipeline_factory import pipeline_factory

router = APIRouter()

@router.post("/", response_model=PipelineResult)
async def answer_question(request: QuestionAnsweringRequest):
    # TODO: Implement question answering
    return PipelineResult(success=True, data={"answer": "Not implemented yet"})