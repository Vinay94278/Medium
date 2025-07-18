# 🗣️ Groq-LangChain Translator (Beginner-Friendly Project)

## 🚀 Project Overview

This is a **GenAI Translator App** built using:

* **Groq LLM (LLaMA3 via Groq API)**
* **LangChain**
* **Python (Jupyter Notebook + Modular Python Files)**

It is designed for **beginners** who want to learn how to:

* Use LLMs practically
* Setup clean project structures
* Write scalable and maintainable code

This project also helps in understanding **LLM workflows step-by-step**.

---

## 📂 Folder Structure

```
genai_translator_groq/
│
├── .venv/                   # Virtual environment (local, do not push)
├── .env                     # API keys and configuration
├── requirements.txt         # Project dependencies
├── Langchain Translator
├── ├── Readme.md (Currently Here)
├── ├── translator.ipynb
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/vinayadatiya/GenAI-Langchain-Tutorials.git
cd genai_translator_groq
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
# Activate on Mac/Linux:
source .venv/bin/activate
# Activate on Windows:
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 .env File Example

Create a `.env` file in the root folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🎯 Features

* **LLM Translation using Groq's LLaMA3**
* **Beginner-friendly interactive notebook**
* **Modular, clean code for scaling to production later**
* **Error handling and generic exception management**

---

## 🚧 Current Limitations

* No token usage tracking (LangSmith will be added later)
* Notebook-only backend (no REST API yet)
* No UI (Streamlit frontend will be covered in upcoming sessions)

---

## 📚 References & Learning Resources

* [LangChain Docs](https://python.langchain.com/docs/)
* [Groq API Console](https://console.groq.com/)
* [LangSmith (Tracing & Debugging)](https://docs.smith.langchain.com/)

---

## 🔮 What’s Next?

In the next sessions, we'll cover:

* **LangSmith for observability**
* **ChatModels & Message Roles deeper**
* **Building a full RAG Pipeline**

---

## 👋 About Me

I’m **Vinay Adatiya**, passionate about sharing **GenAI knowledge in a simple and practical way**.

* **LinkedIn**: [Vinay's Linkedin](https://www.linkedin.com/in/vinay-adatiya/)
* **Medium**: [Vinay's Medium](https://medium.com/@adatiyavinayshaileshbhai)
* **GitHub**: [Vinay's GitHub](https://github.com/Vinay94278)

Feel free to fork, star, or contribute to the project!