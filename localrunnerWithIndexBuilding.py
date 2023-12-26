from pathlib import Path
import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    download_loader,
)
from llama_index.llms import Ollama
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

# more info to the JSONReader https://llamahub.ai/l/file-json?from=all
JSONReader = download_loader("JSONReader")
loader = JSONReader()
#need better input we do not want re-create Tay
#CHANGE HERE##########################
documents = loader.load_data(Path('./data/tinytweets.json'))

#load this date into the Qdrant vector database. 
# more info: https://github.com/qdrant/qdrant
client = qdrant_client.QdrantClient(
    path="./qdrant_data"
)

#create the contex
vector_store = QdrantVectorStore(client=client, collection_name="tweets")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

#create the index for later query
index = VectorStoreIndex.from_documents(documents,service_context=service_context,storage_context=storage_context)

query_engine = index.as_query_engine()
#the q 
response = query_engine.query("What does the author think about Star Trek? Give details.")
print(response)
