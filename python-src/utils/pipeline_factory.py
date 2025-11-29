from transformers import pipeline
import asyncio
import logging
from typing import Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor
import torch

logger = logging.getLogger(__name__)

class PipelineFactory:
    def __init__(self):
        self.pipelines: Dict[str, Any] = {}
        self.is_initializing: Dict[str, asyncio.Future] = {}
        self.executor = ThreadPoolExecutor(max_workers=4)
        self.device = 0 if torch.cuda.is_available() else -1
        logger.info(f"Using device: {'cuda' if self.device == 0 else 'cpu'}")

    async def initialize(self):
        """Initialize the pipeline factory"""
        logger.info("PipelineFactory initialized")

    async def get_pipeline(self, task: str, model: Optional[str] = None) -> Any:
        """
        Get or create a pipeline for the given task and model.
        Uses caching to avoid recreating pipelines.
        """
        key = f"{task}:{model or 'default'}"

        # Return cached pipeline if available
        if key in self.pipelines:
            return self.pipelines[key]

        # If already initializing, wait for it
        if key in self.is_initializing:
            return await self.is_initializing[key]

        # Initialize new pipeline
        future = asyncio.get_event_loop().create_future()
        self.is_initializing[key] = future

        try:
            # Run pipeline creation in thread pool to avoid blocking
            loop = asyncio.get_event_loop()
            pipe = await loop.run_in_executor(
                self.executor,
                self._create_pipeline,
                task,
                model
            )

            self.pipelines[key] = pipe
            future.set_result(pipe)
            del self.is_initializing[key]
            return pipe

        except Exception as error:
            future.set_exception(error)
            del self.is_initializing[key]
            raise error

    def _create_pipeline(self, task: str, model: Optional[str] = None) -> Any:
        """Create a pipeline in a separate thread"""
        logger.info(f"Creating pipeline for task: {task}, model: {model}")
        try:
            if model:
                return pipeline(
                    task=task,
                    model=model,
                    device=self.device,
                    torch_dtype=torch.float16 if self.device == 0 else torch.float32
                )
            else:
                return pipeline(
                    task=task,
                    device=self.device,
                    torch_dtype=torch.float16 if self.device == 0 else torch.float32
                )
        except Exception as error:
            logger.error(f"Failed to create pipeline for {task}: {error}")
            raise error

    def clear_cache(self):
        """Clear all cached pipelines"""
        self.pipelines.clear()
        self.is_initializing.clear()
        logger.info("Pipeline cache cleared")

    def get_cached_pipelines(self) -> list[str]:
        """Get list of cached pipeline keys"""
        return list(self.pipelines.keys())

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.executor.shutdown(wait=True)

# Global instance
pipeline_factory = PipelineFactory()