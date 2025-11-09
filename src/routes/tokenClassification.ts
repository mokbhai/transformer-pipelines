import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type {
  TokenClassificationRequest,
  PipelineResult,
} from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text }: TokenClassificationRequest = req.body;

    if (!text) {
      return res.status(400).json({ error: "Missing required field: text" });
    }

    const pipe = await pipelineFactory.getPipeline("token-classification");
    const result = await pipe(text);

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Token classification failed",
    });
  }
});

export default router;
