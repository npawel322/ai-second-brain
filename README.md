# 🧠 AI Second Brain (Local RAG)

Personalny asystent oparty o architekturę **RAG (Retrieval-Augmented Generation)**, który pozwala na interakcję z prywatnymi dokumentami w trybie 100% offline.

## 🚀 Kluczowe Cechy
- **Pełna Prywatność:** Dzięki wykorzystaniu lokalnych modeli, żadne dane nie opuszczają Twojego komputera.
- **Hybrid Search:** Wykorzystanie bazy wektorowej Qdrant do szybkiego wyszukiwania kontekstowego.
- **Interfejs Streamlit:** Przejrzysty czat w przeglądarce umożliwiający wygodną pracę z bazą wiedzy.

## 🛠️ Stack Technologiczny
- **LLM:** Llama 3 (via Ollama)
- **Framework:** LlamaIndex
- **Baza Wektorowa:** Qdrant (uruchomiony w Dockerze)
- **Embedding Model:** BAAI/bge-small-en-v1.5
- **Frontend:** Streamlit

## ⚙️ Jak uruchomić?

### 1. Wymagania
- Zainstalowany [Docker](https://www.docker.com/)
- Zainstalowana [Ollama](https://ollama.com/)

### 2. Konfiguracja bazy i modelu
```bash
# Uruchomienie bazy Qdrant
docker run -p 6333:6333 qdrant/qdrant

# Pobranie modelu Llama 3
ollama pull llama3

```
## 📺 Demo
![AI Second Brain Demo](assets/demo.mp4)
