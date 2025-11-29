from fastapi import APIRouter, HTTPException
from utils.pipeline_factory import pipeline_factory
from models.types import ImageToTextRequest, PipelineResult
import base64
import io
from PIL import Image
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

def decode_base64_image(base64_string: str) -> Image.Image:
    """Decode base64 string to PIL Image"""
    try:
        # Remove data URL prefix if present
        if "data:image" in base64_string:
            base64_string = base64_string.split(",")[1]

        image_data = base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(image_data))
        return image
    except Exception as e:
        raise ValueError(f"Failed to decode image: {str(e)}")

@router.post("/", response_model=PipelineResult)
async def image_to_text(request: ImageToTextRequest):
    """Convert image to text using transformer pipeline"""
    try:
        if not request.image_data:
            raise HTTPException(
                status_code=400,
                detail="Missing required field: image_data"
            )

        # Decode the image
        image = decode_base64_image(request.image_data)

        # Get the pipeline
        pipe = await pipeline_factory.get_pipeline("image-to-text")

        # Prepare generation parameters
        generation_kwargs = {}
        if request.generation:
            if request.generation.max_new_tokens:
                generation_kwargs["max_new_tokens"] = request.generation.max_new_tokens
            if request.generation.num_beams:
                generation_kwargs["num_beams"] = request.generation.num_beams
            if request.generation.temperature:
                generation_kwargs["temperature"] = request.generation.temperature
            if request.generation.top_k:
                generation_kwargs["top_k"] = request.generation.top_k
            if request.generation.do_sample is not None:
                generation_kwargs["do_sample"] = request.generation.do_sample

        # Run the pipeline
        if generation_kwargs:
            result = pipe(image, **generation_kwargs)
        else:
            result = pipe(image)

        return PipelineResult(success=True, data=result)

    except ValueError as e:
        logger.error(f"Image decoding error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Image to text pipeline error: {e}")
        return PipelineResult(
            success=False,
            error=f"Image to text failed: {str(e)}"
        )