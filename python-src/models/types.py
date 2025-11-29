from pydantic import BaseModel
from typing import Optional, List, Any, Dict
from enum import Enum

class GenerationParams(BaseModel):
    max_new_tokens: Optional[int] = None
    num_beams: Optional[int] = None
    temperature: Optional[float] = None
    top_k: Optional[int] = None
    do_sample: Optional[bool] = None
    multi_label: Optional[bool] = None

class TranslationRequest(BaseModel):
    text: str
    language_from: str
    language_to: str
    generation: Optional[GenerationParams] = None

class TextGenerationRequest(BaseModel):
    text: str
    generation: Optional[GenerationParams] = None

class SentimentAnalysisRequest(BaseModel):
    text: str

class QuestionAnsweringRequest(BaseModel):
    context: str
    question: str
    generation: Optional[GenerationParams] = None

class SummarizationRequest(BaseModel):
    text: str
    generation: Optional[GenerationParams] = None

class TokenClassificationRequest(BaseModel):
    text: str

class ZeroShotClassificationRequest(BaseModel):
    text: str
    classes: List[str]
    multi_label: Optional[bool] = False

class MaskedLanguageModelingRequest(BaseModel):
    text: str
    topk: Optional[int] = 5

class CodeCompletionRequest(BaseModel):
    text: str
    generation: Optional[GenerationParams] = None

class ImageToTextRequest(BaseModel):
    image_data: str  # base64 encoded image or URL
    generation: Optional[GenerationParams] = None

class ImageClassificationRequest(BaseModel):
    image_data: str  # base64 encoded image or URL

class ObjectDetectionRequest(BaseModel):
    image_data: str  # base64 encoded image or URL

class OcrRequest(BaseModel):
    image_data: str  # base64 encoded image or URL

class PipelineResult(BaseModel):
    success: bool
    data: Optional[Any] = None
    error: Optional[str] = None

class HealthResponse(BaseModel):
    status: str
    message: str