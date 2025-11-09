import { pipeline } from "@huggingface/transformers";

// Allocate a pipeline for sentiment-analysis
const pipe = await pipeline("sentiment-analysis");

const out = await pipe("I love transformers!");
// [{'label': 'POSITIVE', 'score': 0.999817686}]

console.log(out);