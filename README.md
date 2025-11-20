# Fast Chatbot 🚀

A **minimal, production-ready LLM chatbot** built in a **single `app.py` file**.

This project is designed to help you (and your audience) spin up a fully working AI chatbot in minutes — perfect for:
- Live coding demos
- YouTube / TikTok shorts
- Quick prototypes for clients or internal teams

It uses the **OpenAI API** under the hood and exposes a clean chat interface so you can focus on **prompting and interaction**, not boilerplate.

---

## ✨ Features

- 🧠 **LLM-powered chatbot** using OpenAI models (configurable in `app.py`)
- 💬 **Chat-style interface** with user & assistant messages
- ⚙️ **Configurable system prompt** to control chatbot personality/behavior
- 🔑 **API-key based authentication** (no key stored in code by default)
- 🧩 **Single-file app** – easy to read, teach, and extend
- 🏗️ Great for **fast demos, tutorials, and experimentation**

---

## 🧰 Tech Stack

- **Language:** Python 3.x  
- **Core Libraries:**  
  - `openai` (or `openai` compatible client)
  - Any additional libraries imported in `app.py` (e.g., `streamlit`, `dotenv`, etc. – see your file)

> 🔍 Since the entire logic lives in `app.py`, you can open it to see the exact imports and adjust the steps below accordingly.

---

## 📦 Installation

1. **Clone this repository**

```bash
git clone https://github.com/ishwor2048/fast-chatbot.git
cd fast-chatbot
