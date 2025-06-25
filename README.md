<!-- BEGIN README -->

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

# Gemini-powered FastAPI Microservice

Lightweight REST wrapper around Google Gemini (`models/gemini-1.5-flash` by default) with two endpoints, Swagger docs, and a slim Docker image.

---

## ✨ Features

| Category  | Highlights                                           |
|-----------|------------------------------------------------------|
| Endpoints | `GET /generate?prompt=…` & `POST /generate` (JSON)   |
| Docs      | Swagger UI at **/docs**                              |
| Secrets   | `.env`-based `GEMINI_API_KEY` (never committed)      |
| Docker    | < 40 MB image, ready for compose / cloud             |

---

## 🚀 Quick Start

```bash
# clone & push workflow
git clone https://github.com/Dodo-69764/gemini-fastapi.git
cd gemini-fastapi
# edit … ➜ git push
```

<details>
<summary><strong>Run locally (venv)</strong></summary>

```bash
python -m venv .venv && . .venv/Scripts/activate
pip install -r requirements.txt
echo GEMINI_API_KEY=your_key_here > .env
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
# visit http://localhost:8000/docs
```
</details>

<details>
<summary><strong>Run in Docker</strong></summary>

```bash
docker build -t gemini-fastapi .
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key_here \
  gemini-fastapi
```
</details>

---

## 🖥️ Host Details (LAN)

| Host PC (runs Uvicorn)                                        | Colleague PC (same LAN)                         |
|---------------------------------------------------------------|-------------------------------------------------|
| `uvicorn main:app --host 0.0.0.0 --port 8000`                 | Use host IP e.g. `172.16.0.243`                 |
| Find IP via `ipconfig` → `IPv4 Address`                       | Call `http://172.16.0.243:8000`                 |

Example:

```text
GET  http://172.16.0.243:8000/generate?prompt=Hello
POST http://172.16.0.243:8000/generate
```

---

## 📑 API Reference

| Method | Path / Query                     | Success 200 JSON             |
|--------|----------------------------------|------------------------------|
| GET    | `/generate?prompt=Hello`         | `{ "response": "…" }`        |
| POST   | `/generate` body `{ "prompt":…}` | `{ "response": "…" }`        |

```bash
curl -X POST http://localhost:8000/generate \
     -H "Content-Type: application/json" \
     -d '{ "prompt": "Tell me a fun fact about space." }'
```

---

## 🔧 Environment Variables

| Key              | Required | Purpose                           |
|------------------|----------|-----------------------------------|
| `GEMINI_API_KEY` | ✅       | Google AI Studio key              |
| `MODEL_ID`       | optional | e.g. `models/gemini-2.5-flash`    |

`.env` example:

```env
GEMINI_API_KEY=AIza...your_key...
MODEL_ID=models/gemini-1.5-flash
```

---

## 🌍 Public Access Options

| Scenario    | Tool   | Steps                              |
|-------------|--------|------------------------------------|
| Quick demo  | ngrok  | `ngrok http 8000` → share HTTPS URL|
| Cloud URL   | Render | Connect repo · add key · expose 8000|

---

## ❓ FAQ

<details>
<summary><strong>Why no ngrok on our LAN?</strong></summary>
Running with <code>--host 0.0.0.0</code> and sharing the private IP lets colleagues on the same subnet reach the API directly.
</details>

<details>
<summary><strong>Change the Gemini model?</strong></summary>
Set <code>MODEL_ID</code> in <code>.env</code> or via Docker:

```bash
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=$KEY \
  -e MODEL_ID=models/gemini-2.5-flash \
  gemini-fastapi
```
</details>

<details>
<summary><strong>Is my API key safe?</strong></summary>
The key lives only in <code>.env</code> or container env vars, ignored by Git. Rotate it if it leaks.
</details>

<p align="center">Made with ❤️ + FastAPI + Gemini</p>

<!-- END README -->
