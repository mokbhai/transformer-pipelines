import { Router } from "express";
import type { Request, Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type { TranslationRequest, PipelineResult } from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { text, languageFrom, languageTo, generation }: TranslationRequest =
      req.body;

    if (!text || !languageFrom || !languageTo) {
      return res.status(400).json({
        error: "Missing required fields: text, languageFrom, languageTo",
      });
    }

    const pipe = await pipelineFactory.getPipeline("translation");
    const result = await pipe(text, {
      src_lang: languageFrom,
      tgt_lang: languageTo,
      ...generation,
    });

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Translation failed",
    });
  }
});

export default router;
