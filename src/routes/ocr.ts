import { Router } from "express";
import type { Request, Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type { PipelineResult } from "../types/index";

const router = Router();

interface OCRRequest {
  imageData: string; // base64 or URL
}

router.post("/", async (req: Request, res: Response) => {
  try {
    const { imageData }: OCRRequest = req.body;

    if (!imageData) {
      return res
        .status(400)
        .json({ error: "Missing required field: imageData" });
    }

    const pipe = await pipelineFactory.getPipeline(
      "image-to-text",
      "lightonai/LightOnOCR-1B-1025"
    );
    const result = await pipe({
      image: imageData,
    });

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "OCR processing failed",
    });
  }
});

export default router;
