# 🧠 SQL Critique Assistant

A LangGraph-powered assistant that converts natural language into SQL, critiques query quality, and suggests improvements — all via fast, modular REST APIs.

---

## 🚀 Features

- 🗣️ `/ask` – Convert natural language into SQL with critique and explanation  
- 🧠 `/critique` – Analyze and improve raw SQL queries  
- ⚡ `/generate-sql` – Quickly generate SQL from a user question (no critique)  
- 🧪 Includes rich test cases for evaluation and demo

---

## 🏗 Tech Stack

- **LangGraph** – Graph-based flow control  
- **LangChain + OpenAI (GPT-4 / 3.5)** – LLM-backed generation  
- **FastAPI** – Web API framework  
- **Pydantic** – State modeling & validation  
- **Python 3.11**

---

## 🛠 Getting Started

### 1. Clone and set up the project

<pre><code>bash
git clone https://github.com/yourusername/sql-critique-assistant.git
cd sql-critique-assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
</code></pre>

### 2. Set your OpenAI key

Create a `.env` file in the root:

<pre><code>env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
</code></pre>

### 3. Run the server

<pre><code>bash
uvicorn api.main:app --reload
</code></pre>

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test the API.

---

## 🧪 Example Usage

<pre><code>bash
curl -X POST http://localhost:8000/critique \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT * FROM users;"}'

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "How many users signed up last month?"}'
</code></pre>

---

## 📜 License

MIT License

---

## 🙋‍♀️ Author

Built by **Arpitha Bhat**  
*MS in Information Systems | Full Stack & Cloud Developer*
