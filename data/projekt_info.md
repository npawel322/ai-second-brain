# Projekt: AI Second Brain
**Status:** W budowie (Luty 2026)
**Technologia:** RAG (Retrieval-Augmented Generation)

## Cele projektu:
1. Stworzenie lokalnej bazy wiedzy opartej o Llama 3.
2. Wykorzystanie Qdrant jako silnika wyszukiwania wektorowego.
3. Pełna prywatność – dane nie opuszczają mojego komputera.

## Architektura:
Dane są dzielone na fragmenty (chunki), a następnie zamieniane na wektory przez model `bge-small-en-v1.5`. Te wektory trafiają do kontenera Docker z bazą Qdrant.