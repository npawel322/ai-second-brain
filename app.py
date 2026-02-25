import qdrant_client
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# 1. Konfiguracja Modeli
print("--- Inicjalizacja modeli... ---")
Settings.llm = Ollama(model="llama3", request_timeout=120.0)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# 2. Połączenie z Dockerem (Qdrant)
print("--- Łączenie z bazą Qdrant... ---")
client = qdrant_client.QdrantClient(host="localhost", port=6333)
vector_store = QdrantVectorStore(client=client, collection_name="second_brain")

# 3. Wczytywanie danych
print("--- Indeksowanie dokumentów z folderu /data... ---")
documents = SimpleDirectoryReader("./data").load_data()
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 4. Tworzenie indeksu
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

# 5. Zapytanie
query_engine = index.as_query_engine()
pytanie = "Jakie technologie są wykorzystywane w tym projekcie?"
print(f"--- Zadawanie pytania: {pytanie} ---")

response = query_engine.query(pytanie)

print("\n--- ODPOWIEDŹ AI ---")
print(response)