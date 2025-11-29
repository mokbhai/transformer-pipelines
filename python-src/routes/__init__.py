# Routes package
from .translation import router as translation
from .text_generation import router as text_generation
from .sentiment_analysis import router as sentiment_analysis
from .question_answering import router as question_answering
from .summarization import router as summarization
from .token_classification import router as token_classification
from .zero_shot_classification import router as zero_shot_classification
from .masked_language_modeling import router as masked_language_modeling
from .code_completion import router as code_completion
from .image_to_text import router as image_to_text
from .image_classification import router as image_classification
from .object_detection import router as object_detection
from .ocr import router as ocr