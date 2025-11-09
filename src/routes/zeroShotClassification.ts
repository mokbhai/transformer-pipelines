import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type {
  ZeroShotClassificationRequest,
  PipelineResult,
} from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text, classes, multiLabel }: ZeroShotClassificationRequest =
      req.body;

    if (!text || !classes || classes.length === 0) {
      return res.status(400).json({
        error: "Missing required fields: text, classes (non-empty array)",
      });
    }

    const pipe = await pipelineFactory.getPipeline("zero-shot-classification");
    const result = await pipe(text, classes, {
      multi_label: multiLabel ?? false,
    });

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Zero-shot classification failed",
    });
  }
});

export default router;
