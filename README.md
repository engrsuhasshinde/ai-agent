# 🤖 AI Coding Assistant with Memory (Mini RAG System)

A command-driven AI assistant built using local LLMs that supports chat history persistence, memory retrieval, and context-grounded responses.

This project is a step toward understanding how real-world GenAI systems handle memory and retrieval.

---

## 🚀 Features

- Interactive CLI-based chat assistant  
- Persistent chat storage (JSON, timestamp-based)  
- Memory retrieval using commands:
  - /load all: <query>
  - /load range from YYYY-MM-DD to YYYY-MM-DD: <query>  
- Keyword-based search with ranking  
- Context injection for grounded responses (reduces hallucination)  
- Streaming responses (real-time output)  
- Safe file handling and error handling  

---

## 🧠 How It Works

### 1. Chat Storage
Each session is stored as a JSON file:

chat_history/chat_YYYY-MM-DD_HH-MM-SS.json

---

### 2. Memory Retrieval

You can explicitly query past conversations:

/load all: sample chat

/load range from 2026-05-01 to 2026-05-05: error handling

---

### 3. Retrieval + Grounding (Mini RAG)

- Relevant past messages are retrieved using keyword matching  
- Results are ranked based on relevance  
- Retrieved context is injected into the model prompt  
- Model is instructed to:
  - Use only retrieved context  
  - Avoid hallucination  
  - Return exact matches when possible  

---

## 🏗️ Tech Stack

- Python  
- OpenAI-compatible client (Ollama)  
- Local LLM (phi4-mini)  
- JSON for storage  

---

## ▶️ Getting Started

### 1. Install dependencies

pip install openai

---

### 2. Run model (Ollama)

ollama run phi4-mini

---

### 3. Run the assistant

python agent.py

---

## 💡 Example Usage

You: hi  
Assistant: Hello! How can I assist you today?

You: /load all: sample chat  
Searching past conversations...

Assistant: sample chat 3

---

## ⚠️ Challenges Solved

- Prompt pollution (model storing its own prompts)  
- Memory contamination (AI-generated content being reused)  
- Weak grounding (model ignoring context)  

---

## 🔮 Future Improvements

- Semantic search using embeddings (FAISS / vector DB)  
- Better ranking (TF-IDF / cosine similarity)  
- Metadata-based filtering  
- Web UI (Streamlit / React)  
- Structured memory  

---

## 🧠 Key Takeaway

Separating stored data from model input is critical for building reliable AI systems.

---

## 📌 Author

Suhas Shinde

---

## ⭐ If you found this useful

Give it a star and feel free to contribute!
