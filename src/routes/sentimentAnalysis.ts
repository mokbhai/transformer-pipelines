import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type { SentimentAnalysisRequest, PipelineResult } from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text }: SentimentAnalysisRequest = req.body;

    if (!text) {
      return res.status(400).json({ error: "Missing required field: text" });
    }

    const pipe = await pipelineFactory.getPipeline("sentiment-analysis");
    const result = await pipe(text);

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Sentiment analysis failed",
    });
  }
});

export default router;
