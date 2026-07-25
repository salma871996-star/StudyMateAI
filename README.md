
# StudyMateAI
# 🚀 [Tips Hindawi](https://www.tipshindawi.com/) Challenge (June–July) 2026

> 🏆 This repository is my official submission for the [ **Tips Hindawi** ](https://www.tipshindawi.com/) **Challenge (June–July) 2026**.

## 👤 Participant

| Field            | Value                                |
| ---------------- | ------------------------------------ |
| Full Name        |      Salma Ahmed Hassan                                |
| Project Name     |      StudyMate AI                          |
| GitHub Username  |      salma871996-star                       |
| Challenge Batch  | June–July 2026                       |
| Training Program | Large Language Models (LLMs) Program |
| Organization     | [**Edrak for Ai**](https://edrak4ai.com/en)                         |

---

# 📖 Project Overview

**StudyMate AI** is an AI-powered learning assistant acts as a complete study system designed to solve one of the biggest challenges students face: **lecture backlog** caused by lengthy, information-heavy PDF lectures. Many students postpone studying because traditional lecture PDFs are difficult to read, overwhelming, difficult to digest and time-consuming.

This all-in-one comprehensive learning management and study assistant platform engineered to support students across every aspect of their academic journey by combining AI-powered note generation, summarization, question answering, quiz generation, and personalized study planning based on the number of days and study hours chosen by the student into a single platform, StudyMate AI makes studying faster, easier, and more effective while reducing the stress of dealing with heavy lecture PDFs.
---

# ✨ Features

* 📄 **Smart PDF Processing:** Load and process multi-page lecture PDFs using `PyPDFLoader` and intelligent text chunking.
* 💬 **Context-Aware Q&A (RAG):** Ask any question about your lectures and get precise, accurate answers generated via `Mistral-7B-Instruct` and backed by `FAISS` vector database.
* 📝 **Automatic Summarization:** Instantly generate clear, structured summaries of entire lectures to capture core ideas.
* 📑 **Structured Study Notes:** Automatically extract key concepts, formulas, and definitions formatted into easy-to-read study notes with bullet points.
* ❓ **Interactive MCQ Generator:** Test your knowledge after studying with automatically generated multiple-choice quizzes (MCQs) tailored directly from the uploaded content.
* 📅 **Personalized Study Planner:** Generate custom, step-by-step revision schedules based on your exam or next lecture date and daily available study hours.
* 🔒 **Secure FastAPI Backend:** Fully equipped with authorization headers (API Key) and tunneled via `pyngrok` for seamless integration with the Streamlit frontend.

---

# 🛠️ Technologies Used

### 🤖 AI & Machine Learning Pipeline
* ![Hugging Face](https://img.shields.io/badge/-Hugging%20Face-FFD21E?style=flat&logo=huggingface&logoColor=black) **Hugging Face Transformers:** Powered by `mistralai/Mistral-7B-Instruct-v0.2` for text generation, Q&A, and planning.
* ![LangChain](https://img.shields.io/badge/-LangChain-1C3C3C?style=flat&logo=langchain&logoColor=white) **LangChain:** Orchestrates the RAG workflow, text splitters, prompt templates, and chain execution.
* **Sentence-Transformers:** Uses `all-MiniLM-L6-v2` to generate semantic embeddings for document chunks.
* **FAISS (Facebook AI Similarity Search):** CPU-optimized vector database for high-performance similarity search and indexing.

### ⚙️ Backend & API Development
* ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat&logo=fastapi&logoColor=white) **FastAPI:** High-performance RESTful API powering all processing endpoints.
* ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) **Python 3.10+:** Core language used across the entire backend logic and AI pipeline.
* **Pyngrok:** Exposes the local FastAPI server securely via a public tunnel.
* **PyPDF:** PDF extraction and parsing engine.

### 🎨 Frontend & User Interface
* ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) **Streamlit:** Clean, interactive UI for file uploads, chat interface, quiz generation, and plan views.

---

# ⚙️ Installation 

Follow these steps to set up and run **StudyMate AI** on your local machine.



### 📋 Prerequisites
* **Python 3.10+** installed on your system.
* A free **Ngrok Account** and Authtoken (for backend tunneling).



### 1. Clone the Repository
```bash
git clone https://github.com/salma871996-star/StudyMate_AI.git
cd StudyMate_AI
```
---

# 🚀 Usage Guide


### 1. 📤 Upload Lecture
Upload your course PDF via the sidebar. The system extracts text and builds a FAISS index automatically.


### 2. 💬 AI Chat (RAG)
Ask any question about the lecture to get accurate, context-based answers without hallucinations.


### 3. 📝 Summaries
Generate structured summaries, main takeaways.

### 4. 📝 Notes
Generate all lecture details into clear, easy-to-study notes.

### 5. ❓ Practice Quiz
Generate multiple-choice quizzes (MCQs) directly from your material to test your understanding.



### 6. 📅 Custom Study Plan
Input your exam date and daily study hours to receive a personalized study schedule.

---

# 📸 Demo

Here is a quick look at **StudyMate AI** in action:
<img width="3682" height="1550" alt="Screenshot 2026-07-25 051546" src="https://github.com/user-attachments/assets/e46b6cd9-1aca-4524-887d-7b8667e76c14" />

<!-- Add your image here on GitHub -->

* **Interactive Interface:** Upload PDFs, chat with your materials, and generate quizzes or study plans effortlessly.

---

# 📈 Results


* **Fast Retrieval:** Delivers accurate, context-aware answers from uploaded lecture PDFs in seconds using RAG and FAISS.
* **Zero Hallucination:** Ensures responses are strictly grounded in the provided course materials.
* **All-in-One Study Hub:** Seamlessly combines PDF Q&A, automatic study notes, MCQ quiz generation, and personalized study planning in a single interface.

---

# 🔮 Future Improvements


* **Multi-Modal Support:** Add the ability to process lecture videos, audio recordings, and hand-written diagram images.
* **Multi-Document Chat:** Allow users to upload and query multiple lectures or entire course modules simultaneously.


---

# 📚 About the Challenge

This project was developed as part of the [**Tips Hindawi**](https://www.tipshindawi.com/) **Challenge (June–July) 2026**.

[Tips Hindawi](https://www.tipshindawi.com/) is the internships department of [**Edrak for Ai**](https://edrak4ai.com/en), and the challenge encourages participants to build real-world projects, apply practical skills, and showcase their work through GitHub.

For more information about the challenge, training programs, and upcoming batches, visit the official [Tips Hindawi](https://www.tipshindawi.com/) website.

---

# 📄 License

This project is shared for educational and portfolio purposes.
