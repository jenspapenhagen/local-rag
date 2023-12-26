# local-rag
loading the model [dolphin-2.5-mixtral-8x7b](https://huggingface.co/TheBloke/dolphin-2.5-mixtral-8x7b-GGUF)
local into [ollama](https://ollama.ai/)
and buildup a small RAG (Retrieval Augmented Generation)
with [llama-index](https://github.com/run-llama/llama_index)
and as DB we use [qdrant](https://github.com/qdrant/qdrant)
for the up-to-date personal-data.

> [!WARNING]  
> this is only a collection of python/bash scripts

### What is retrieval-augmented generation? ###
RAG is an AI framework for retrieving facts from an external knowledge base to ground large language models (LLMs) 
on the most accurate, up-to-date information and to give users insight into LLMs' generative process.
