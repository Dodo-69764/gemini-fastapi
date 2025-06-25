<p align="center">
  <!-- Optional banner image — replace or remove -->
  <!-- <img src="https://raw.githubusercontent.com/Dodo-69764/gemini-fastapi/main/.github/banner.svg" width="640" alt="Gemini FastAPI"> -->
</p>

<p align="center">
  <a href="https://github.com/Dodo-69764/gemini-fastapi/actions">
    <img alt="CI" src="https://github.com/Dodo-69764/gemini-fastapi/actions/workflows/ci.yml/badge.svg">
  </a>
  <a href="https://hub.docker.com/r/dodo69764/gemini-fastapi">
    <img alt="Docker Pulls" src="https://img.shields.io/docker/pulls/dodo69764/gemini-fastapi?logo=docker">
  </a>
  <img alt="Python ≥3.10" src="https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white">
  <img alt="FastAPI" src="https://img.shields.io/badge/FastAPI-0.115.13-teal?logo=fastapi">
</p>

---

# Gemini-powered FastAPI Microservice

*A lightweight REST wrapper around Google Gemini (default model `models/gemini-1.5-flash`) with two endpoints, auto-docs, and Docker support.*

---

## ✨ Features

| Category         | Highlights                                                         |
|------------------|--------------------------------------------------------------------|
| **Endpoints**    | `GET /generate?prompt=…` &nbsp;·&nbsp; `POST /generate` (JSON)     |
| **Docs**         | Swagger UI at **/docs**                                            |
| **Secrets**      | Loads **GEMINI_API_KEY** from `.env` (never committed)             |
| **Docker**       | < 40 MB image from `python:3.10-slim`                              |
| **Reproducible** | Fully pinned `requirements.txt`                                    |

---

## 🚀 Quick Start

```bash
# clone / push workflow
git clone https://github.com/Dodo-69764/gemini-fastapi.git
cd gemini-fastapi
# (edit code, docs …) ➜ git push

<details> <summary><strong>Run locally (venv)</strong></summary>
bash
Copy
Edit
python -m venv .venv && . .venv/Scripts/activate
pip install -r requirements.txt
echo GEMINI_API_KEY=your_key_here > .env
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Visit http://localhost:8000/docs in your browser.

</details> <details> <summary><strong>Run in Docker</strong></summary>
bash
Copy
Edit
docker build -t gemini-fastapi .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key_here gemini-fastapi
</details>

🖥️ Host Details (LAN)
Host PC (runs Uvicorn)	Colleague PC (same LAN)
Start with <code>uvicorn main:app --host 0.0.0.0 --port 8000</code>	Use host’s IP (e.g. 172.16.0.243)
Find IP via ipconfig → IPv4 Address (e.g. 172.16.0.243)	Call:
http://172.16.0.243:8000
Example for colleagues

nginx
Copy
Edit
GET  http://172.16.0.243:8000/generate?prompt=Hello
POST http://172.16.0.243:8000/generate
📑 API Reference
Method	Path / Query	Success 200 (JSON)
GET	/generate?prompt=Hello	{ "response": "..." }
POST	/generate Body { "prompt": "Hi" }	{ "response": "..." }

bash
Copy
Edit
# cURL example
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -d '{ "prompt": "Tell me a fun fact about space." }'
🔧 Environment Variables
Key	Required	Purpose
GEMINI_API_KEY	✅	Google AI Studio key
MODEL_ID	optional	Override model (e.g. models/gemini-2.5-flash)

.env example:

env
Copy
Edit
GEMINI_API_KEY=AIza...your_key...
MODEL_ID=models/gemini-1.5-flash
🌍 Public Access Options
Scenario	Tool	Steps
Quick demo	ngrok	ngrok http 8000 → share HTTPS URL
Cloud URL	Render / Fly.io	Connect repo · add GEMINI_API_KEY · expose 8000

❓ FAQ
<details> <summary><strong>Why isn’t ngrok needed on our LAN?</strong></summary>
Running Uvicorn with <code>--host 0.0.0.0</code> and sharing your private
IP lets colleagues on the same subnet reach the API directly.

</details> <details> <summary><strong>How do I change the Gemini model?</strong></summary>
Set <code>MODEL_ID</code> in <code>.env</code> or pass via Docker:

bash
Copy
Edit
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=$KEY \
  -e MODEL_ID=models/gemini-2.5-flash \
  gemini-fastapi
</details> <details> <summary><strong>Is my API key safe?</strong></summary>
The key lives only in <code>.env</code> or container env vars, ignored by Git.
If it leaks, rotate it in Google AI Studio.

</details>
<p align="center">Made with ❤️ + FastAPI + Gemini</p> ```
How to use
Create/overwrite README.md in your project root with the block above.

Save the file.

Commit & push:

bash
Copy
Edit
git add README.md
git commit -m "docs: comprehensive README with host details & FAQ"
git push