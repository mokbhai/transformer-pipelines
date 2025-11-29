from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import time
from contextlib import asynccontextmanager

from utils.pipeline_factory import pipeline_factory
from routes import (
    translation,
    text_generation,
    sentiment_analysis,
    question_answering,
    summarization,
    token_classification,
    zero_shot_classification,
    masked_language_modeling,
    code_completion,
    image_to_text,
    image_classification,
    object_detection,
    ocr
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("Initializing PipelineFactory...")
    await pipeline_factory.initialize()
    logger.info("Server startup complete")
    yield
    # Shutdown
    logger.info("Server shutting down")

app = FastAPI(
    title="Transformer Pipelines API",
    description="FastAPI server for Hugging Face transformer pipelines",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    logger.info(f"{request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time
    logger.info(f"Completed in {process_time:.2f}s - Status: {response.status_code}")

    return response

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "Server is running"}

# API Routes
app.include_router(translation, prefix="/api/translation", tags=["translation"])
app.include_router(text_generation, prefix="/api/text-generation", tags=["text-generation"])
app.include_router(sentiment_analysis, prefix="/api/sentiment-analysis", tags=["sentiment-analysis"])
app.include_router(question_answering, prefix="/api/question-answering", tags=["question-answering"])
app.include_router(summarization, prefix="/api/summarization", tags=["summarization"])
app.include_router(token_classification, prefix="/api/token-classification", tags=["token-classification"])
app.include_router(zero_shot_classification, prefix="/api/zero-shot-classification", tags=["zero-shot-classification"])
app.include_router(masked_language_modeling, prefix="/api/masked-language-modeling", tags=["masked-language-modeling"])
app.include_router(code_completion, prefix="/api/code-completion", tags=["code-completion"])
app.include_router(image_to_text, prefix="/api/image-to-text", tags=["image-to-text"])
app.include_router(image_classification, prefix="/api/image-classification", tags=["image-classification"])
app.include_router(object_detection, prefix="/api/object-detection", tags=["object-detection"])
app.include_router(ocr, prefix="/api/ocr", tags=["ocr"])

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error"}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )