export interface TranslationRequest {
  text: string;
  languageFrom: string;
  languageTo: string;
  generation?: GenerationParams;
}

export interface TextGenerationRequest {
  text: string;
  generation?: GenerationParams;
}

export interface SentimentAnalysisRequest {
  text: string;
}

export interface QuestionAnsweringRequest {
  context: string;
  question: string;
  generation?: GenerationParams;
}

export interface SummarizationRequest {
  text: string;
  generation?: GenerationParams;
}

export interface TokenClassificationRequest {
  text: string;
}

export interface ZeroShotClassificationRequest {
  text: string;
  classes: string[];
  multiLabel?: boolean;
}

export interface MaskedLanguageModelingRequest {
  text: string;
  topk?: number;
}

export interface CodeCompletionRequest {
  text: string;
  generation?: GenerationParams;
}

export interface ImageToTextRequest {
  imageData: string; // base64 or URL
  generation?: GenerationParams;
}

export interface ImageClassificationRequest {
  imageData: string; // base64 or URL
}

export interface ObjectDetectionRequest {
  imageData: string; // base64 or URL
}

export interface GenerationParams {
  max_new_tokens?: number;
  num_beams?: number;
  temperature?: number;
  top_k?: number;
  do_sample?: boolean;
  multi_label?: boolean;
}

export interface PipelineResult {
  success: boolean;
  data?: any;
  error?: string;
}
