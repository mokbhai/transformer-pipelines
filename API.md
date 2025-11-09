# Transformer Pipelines - Express Server API

This is a Bun/Node.js Express server that exposes APIs for various transformer models from Hugging Face.

## Getting Started

### Installation

```bash
bun install
```

### Running the Server

**Development mode (with auto-reload):**

```bash
bun run dev
```

**Production mode:**

```bash
bun start
```

The server will start on `http://localhost:3000`

## API Endpoints

### Health Check

```
GET /health
```

### Translation

```
POST /api/translation
Content-Type: application/json

{
  "text": "Hello, how are you?",
  "languageFrom": "en",
  "languageTo": "fr",
  "generation": {
    "max_new_tokens": 200,
    "num_beams": 1,
    "temperature": 1,
    "top_k": 0,
    "do_sample": false
  }
}
```

### Text Generation

```
POST /api/text-generation
Content-Type: application/json

{
  "text": "I enjoy walking with my cute dog,",
  "generation": {
    "max_new_tokens": 100,
    "num_beams": 1,
    "temperature": 1,
    "top_k": 20,
    "do_sample": true
  }
}
```

### Sentiment Analysis

```
POST /api/sentiment-analysis
Content-Type: application/json

{
  "text": "The Shawshank Redemption is a true masterpiece of cinema"
}
```

### Question Answering

```
POST /api/question-answering
Content-Type: application/json

{
  "context": "The Amazon rainforest is a moist broadleaf forest...",
  "question": "What is the Amazon rainforest?"
}
```

### Summarization

```
POST /api/summarization
Content-Type: application/json

{
  "text": "The tower is 324 metres tall...",
  "generation": {
    "max_new_tokens": 50,
    "num_beams": 2,
    "temperature": 1,
    "top_k": 0,
    "do_sample": false
  }
}
```

### Token Classification (Named Entity Recognition)

```
POST /api/token-classification
Content-Type: application/json

{
  "text": "Hugging Face is a technology company founded in 2016 by Clément Delangue"
}
```

### Zero-Shot Classification

```
POST /api/zero-shot-classification
Content-Type: application/json

{
  "text": "I have a problem with my iPhone that needs to be resolved asap!",
  "classes": ["urgent", "not urgent", "phone", "tablet", "microwave"],
  "multiLabel": false
}
```

### Masked Language Modeling

```
POST /api/masked-language-modeling
Content-Type: application/json

{
  "text": "The goal of life is [MASK].",
  "topk": 5
}
```

### Code Completion

```
POST /api/code-completion
Content-Type: application/json

{
  "text": "def fib(n):",
  "generation": {
    "max_new_tokens": 50,
    "num_beams": 1,
    "temperature": 1,
    "top_k": 0,
    "do_sample": false
  }
}
```

### Image to Text

```
POST /api/image-to-text
Content-Type: application/json

{
  "imageData": "data:image/jpeg;base64,...",
  "generation": {
    "max_new_tokens": 50
  }
}
```

### Image Classification

```
POST /api/image-classification
Content-Type: application/json

{
  "imageData": "data:image/jpeg;base64,..."
}
```

### Object Detection

```
POST /api/object-detection
Content-Type: application/json

{
  "imageData": "data:image/jpeg;base64,..."
}
```

### OCR (Optical Character Recognition)

```
POST /api/ocr
Content-Type: application/json

{
  "imageData": "data:image/jpeg;base64,..."
}
```

Extracts text from images using the LightOnOCR-1B-1025 model.

## Response Format

All API endpoints return a consistent response format:

```json
{
  "success": true,
  "data": {
    "result": "..."
  }
}
```

On error:

```json
{
  "success": false,
  "error": "Error message"
}
```

## Environment Variables

- `PORT`: Port number for the server (default: 3000)

## Building for Production

```bash
bun run build
```

This will create an optimized build in the `dist/` directory.

## Technologies Used

- **Bun**: Runtime and package manager
- **Express.js**: Web framework
- **@huggingface/transformers**: Machine learning models
- **TypeScript**: Type-safe JavaScript
- **CORS**: Cross-origin resource sharing
