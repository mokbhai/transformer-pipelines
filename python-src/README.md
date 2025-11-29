# Transformer Pipelines API (Python/FastAPI)

A FastAPI server that provides access to various Hugging Face transformer pipelines for natural language processing and computer vision tasks.

## Features

- **Text Generation**: Generate text using transformer models
- **Translation**: Translate text between languages
- **Sentiment Analysis**: Analyze sentiment of text
- **Question Answering**: Answer questions based on context
- **Summarization**: Summarize long texts
- **Token Classification**: Classify tokens in text (NER, POS tagging)
- **Zero-shot Classification**: Classify text without training
- **Masked Language Modeling**: Fill in masked tokens
- **Code Completion**: Complete code snippets
- **Image to Text**: Generate captions for images
- **Image Classification**: Classify images
- **Object Detection**: Detect objects in images
- **OCR**: Extract text from images

## Installation

1. Install dependencies using uv:

```bash
uv sync
```

This will create a virtual environment and install all dependencies from `pyproject.toml`.

## Usage

### Running the Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

### Health Check

```bash
curl http://localhost:8000/health
```

### API Endpoints

All endpoints accept POST requests with JSON payloads and return results in the following format:

```json
{
  "success": true,
  "data": {...},
  "error": null
}
```

#### Image to Text

```bash
curl -X POST "http://localhost:8000/api/image-to-text/" \
     -H "Content-Type: application/json" \
     -d '{
       "image_data": "base64_encoded_image_data"
     }'
```

## Architecture

- **FastAPI**: Modern Python web framework
- **Transformers**: Hugging Face transformers library
- **Pipeline Factory**: Caches and manages transformer pipelines
- **Pydantic**: Data validation and serialization
- **Async/Await**: Asynchronous request handling

## Development

The server uses automatic pipeline caching to improve performance. Pipelines are created on-demand and reused for subsequent requests.

## Configuration

- Default port: 8000
- GPU support: Automatically detected
- Model caching: Enabled by default

## License

MIT
