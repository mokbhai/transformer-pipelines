import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type { CodeCompletionRequest, PipelineResult } from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text, generation }: CodeCompletionRequest = req.body;

    if (!text) {
      return res.status(400).json({ error: "Missing required field: text" });
    }

    const pipe = await pipelineFactory.getPipeline(
      "text-generation",
      "Xenova/codegen-350M-mono"
    );
    const result = await pipe(text, generation);

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Code completion failed",
    });
  }
});

export default router;
