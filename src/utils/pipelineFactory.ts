// import { pipeline } from "@huggingface/transformers";
import { pipeline } from "@xenova/transformers";
class PipelineFactory {
  private pipelines: Map<string, any> = new Map();
  private isInitializing: Map<string, Promise<any>> = new Map();

  async initialize() {
    console.log("Initializing PipelineFactory...");
  }

  async getPipeline(task: string, model?: string) {
    const key = `${task}:${model || "default"}`;

    // Return cached pipeline if available
    if (this.pipelines.has(key)) {
      return this.pipelines.get(key);
    }

    // If already initializing, wait for it
    if (this.isInitializing.has(key)) {
      return this.isInitializing.get(key);
    }

    // Initialize new pipeline
    const initPromise = this.initializePipeline(task, model);
    this.isInitializing.set(key, initPromise);

    try {
      const pipe = await initPromise;
      this.pipelines.set(key, pipe);
      this.isInitializing.delete(key);
      return pipe;
    } catch (error) {
      this.isInitializing.delete(key);
      throw error;
    }
  }

  private async initializePipeline(task: string, model?: string) {
    console.log(`Initializing pipeline for task: ${task}, model: ${model}`);
    try {
      if (model) {
        return await pipeline(task as any, model);
      } else {
        return await pipeline(task as any);
      }
    } catch (error) {
      console.error(`Failed to initialize pipeline for ${task}:`, error);
      throw error;
    }
  }

  clearCache() {
    this.pipelines.clear();
    this.isInitializing.clear();
  }

  getCachedPipelines() {
    return Array.from(this.pipelines.keys());
  }
}

export const pipelineFactory = new PipelineFactory();
