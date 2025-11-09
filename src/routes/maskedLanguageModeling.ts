import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type {
  MaskedLanguageModelingRequest,
  PipelineResult,
} from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text, topk }: MaskedLanguageModelingRequest = req.body;

    if (!text) {
      return res.status(400).json({ error: "Missing required field: text" });
    }

    const pipe = await pipelineFactory.getPipeline("fill-mask");
    const result = await pipe(text, { topk: topk ?? 5 });

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Masked language modeling failed",
    });
  }
});

export default router;
