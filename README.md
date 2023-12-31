# local-rag
loading the model [dolphin-2.5-mixtral-8x7b](https://huggingface.co/TheBloke/dolphin-2.5-mixtral-8x7b-GGUF) as gguf format
local into [ollama](https://ollama.ai/)
and buildup a small RAG (Retrieval Augmented Generation)
with [llama-index](https://github.com/run-llama/llama_index)
and as DB we use [qdrant](https://github.com/qdrant/qdrant)
for the up-to-date personal-data.

> [!WARNING]  
> this is only a collection of python/bash scripts, no guarantee.

## Steps to a personal RAG ##
- install ollama/qdrant (as docker is fine, too)
- download the model from the huggingface page
- run buildLocalModel.sh for creating a compl. model form the gguf file for ollama
- edit/run localrunnerWithoutIndex.py for creating an index in qdrant and fill this with your personal-data (json format are best way to go)
- later use localrunnerWithExistingIndex.py
- testing this terminal output
- run startHttpEndpoint.sh to start a small Flask HTTP Endpoint
- go to http://127.0.0.1:5000/process_form for playing around
- test it with cURL
  
 	```bash
   curl -X POST http://127.0.0.1:5000/process_form -F 'query="What does the author think about Star Trek?"'
  	```
- edit httpEndpoint.py for later customizations

  
### What is retrieval-augmented generation? ###
RAG is an AI framework for retrieving facts from an external knowledge base to ground large language models (LLMs) 
on the most accurate, up-to-date information and to give users insight into LLMs' generative process.
