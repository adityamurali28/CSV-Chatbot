# 📊 CSV Chatbot using LangChain, Ollama, and Chroma

This project is a local, private chatbot that allows natural language querying of `.csv` files using Retrieval-Augmented Generation (RAG). It uses [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com) to run large language models locally, and [Chroma](https://www.trychroma.com/) as the vector store for fast and efficient retrieval.

---



- **LangChain**: Framework for chaining LLMs and tools
- **Ollama (v3.2)**: Local LLM inference engine, eliminating the need for external API keys
- **ChromaDB**: Local vector store for storing and retrieving document embeddings
- **mxbai-embed-large**: Embedding model used to convert CSV data into vector format
- **Car_sales.csv**: Source of structured tabular data for the chatbot

---

## 🚀 Features

- Ask natural language questions about the `.csv` file
- Retrieves relevant rows using vector similarity search
- Uses local models — fully offline and private

---

## 🏗️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/adityamurali28/CSV-Chatbot.git
cd csv-chatbot-langchain
