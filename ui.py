import streamlit as st
import qdrant_client
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings

# Konfiguracja strony
st.set_page_config(page_title="AI Second Brain", page_icon="🧠")
st.title("🧠 Mój Cyfrowy Mózg")

# Inicjalizacja modeli (to samo co w app.py)
@st.cache_resource
def load_index():
    Settings.llm = Ollama(model="llama3", request_timeout=120.0)
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    
    client = qdrant_client.QdrantClient(host="localhost", port=6333)
    vector_store = QdrantVectorStore(client=client, collection_name="second_brain")
    
    # Ładujemy już istniejący indeks z Qdrant
    return VectorStoreIndex.from_vector_store(vector_store=vector_store)

index = load_index()
query_engine = index.as_query_engine(similarity_top_k=5)

# Historia czatu
if "messages" not in st.session_state:
    st.session_state.messages = []

# Wyświetlanie historii
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Okno czatu
if prompt := st.chat_input("O co chcesz zapytać swoje notatki?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Szukam w pamięci..."):
            response = query_engine.query(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": str(response)})