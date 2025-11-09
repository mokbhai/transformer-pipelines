import express from "express";
import type { Request, Response, NextFunction } from "express";
import cors from "cors";
import { pipelineFactory } from "./utils/pipelineFactory";
import { errorHandler } from "./middleware/errorHandler";
import { requestLogger } from "./middleware/requestLogger";
import translationRoutes from "./routes/translation";
import textGenerationRoutes from "./routes/textGeneration";
import sentimentAnalysisRoutes from "./routes/sentimentAnalysis";
import questionAnsweringRoutes from "./routes/questionAnswering";
import summarizationRoutes from "./routes/summarization";
import tokenClassificationRoutes from "./routes/tokenClassification";
import zeroShotClassificationRoutes from "./routes/zeroShotClassification";
import maskedLanguageModelingRoutes from "./routes/maskedLanguageModeling";
import codeCompletionRoutes from "./routes/codeCompletion";
import imageToTextRoutes from "./routes/imageToText";
import imageClassificationRoutes from "./routes/imageClassification";
import objectDetectionRoutes from "./routes/objectDetection";
import ocrRoutes from "./routes/ocr";

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json({ limit: "50mb" }));
app.use(express.urlencoded({ limit: "50mb", extended: true }));
app.use(requestLogger);

// Initialize pipeline factory
pipelineFactory.initialize();

// Health check endpoint
app.get("/health", (req: Request, res: Response) => {
  res.json({ status: "ok", message: "Server is running" });
});

// API Routes
app.use("/api/translation", translationRoutes);
app.use("/api/text-generation", textGenerationRoutes);
app.use("/api/sentiment-analysis", sentimentAnalysisRoutes);
app.use("/api/question-answering", questionAnsweringRoutes);
app.use("/api/summarization", summarizationRoutes);
app.use("/api/token-classification", tokenClassificationRoutes);
app.use("/api/zero-shot-classification", zeroShotClassificationRoutes);
app.use("/api/masked-language-modeling", maskedLanguageModelingRoutes);
app.use("/api/code-completion", codeCompletionRoutes);
app.use("/api/image-to-text", imageToTextRoutes);
app.use("/api/image-classification", imageClassificationRoutes);
app.use("/api/object-detection", objectDetectionRoutes);
app.use("/api/ocr", ocrRoutes);

// 404 handler
app.use((req: Request, res: Response) => {
  res.status(404).json({ error: "Route not found" });
});

// Error handler middleware
app.use(errorHandler);

// Start server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
  console.log(`Health check: http://localhost:${PORT}/health`);
});

export default app;
