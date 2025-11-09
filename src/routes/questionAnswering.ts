import { Router, type Request, type Response } from "express";
import { pipelineFactory } from "../utils/pipelineFactory";
import type { QuestionAnsweringRequest, PipelineResult } from "../types/index";

const router = Router();

router.post("/", async (req: Request, res: Response) => {
  try {
    const { context, question, generation }: QuestionAnsweringRequest =
      req.body;

    if (!context || !question) {
      return res.status(400).json({
        error: "Missing required fields: context, question",
      });
    }

    const pipe = await pipelineFactory.getPipeline("question-answering");
    const result = await pipe({ context, question });

    const response: PipelineResult = {
      success: true,
      data: result,
    };

    res.json(response);
  } catch (error: any) {
    res.status(500).json({
      success: false,
      error: error.message || "Question answering failed",
    });
  }
});

export default router;
