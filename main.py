"""
main.py – Gemini-powered FastAPI microservice
"""

from __future__ import annotations

import os
import traceback
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# 1. Load API key from .env (works no matter where Uvicorn is started)
# ---------------------------------------------------------------------------

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

# ---------------------------------------------------------------------------
# 2. Configure the SDK (works with both ≥0.8 and older versions)
# ---------------------------------------------------------------------------

try:
    genai.configure(api_key=API_KEY, api_version="v1")
except TypeError:  # older SDKs (<0.8) don’t accept api_version
    genai.configure(api_key=API_KEY)

MODEL_ID = "models/gemini-1.5-flash"
MODEL = genai.GenerativeModel(MODEL_ID)

# ---------------------------------------------------------------------------
# 3. FastAPI application
# ---------------------------------------------------------------------------

app = FastAPI(title="Gemini FastAPI Service", version="1.0.0")


class Prompt(BaseModel):
    """Request model for POST /generate."""
    prompt: str


def gemini_answer(prompt: str) -> str:
    """
    Return Gemini's plain-text response for the given prompt.

    Raises
    ------
    HTTPException
        If the Gemini SDK raises any error.
    """
    try:
        response = MODEL.generate_content(prompt)
        return response.text
    except Exception as exc:  # noqa: BLE001  # (broad but converted to 500)
        print("Gemini SDK Error:\n", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/generate")
async def generate_get(prompt: str = Query(..., description="Prompt text")) -> dict[str, str]:
    """GET /generate?prompt=Hello"""
    return {"response": gemini_answer(prompt)}


@app.post("/generate")
async def generate_post(body: Prompt) -> dict[str, str]:
    """POST /generate  with JSON: { "prompt": "Hello" }"""
    return {"response": gemini_answer(body.prompt)}
