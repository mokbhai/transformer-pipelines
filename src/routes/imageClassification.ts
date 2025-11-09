import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type {
  ImageClassificationRequest,
  PipelineResult,
} from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { imageData }: ImageClassificationRequest = req.body;

    if (!imageData) {
      return res
        .status(400)
        .json({ error: "Missing required field: imageData" });
    }

    const pipe = await pipelineFactory.getPipeline("image-classification");
    const result = await pipe(imageData);

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Image classification failed",
    });
  }
});

export default router;
