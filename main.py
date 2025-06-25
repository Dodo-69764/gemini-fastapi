"""
main.py – Gemini-powered FastAPI microservice
"""

import os
from pathlib import Path
import traceback

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

# ───────────────────────────────────────────────────────────────────────────────
# 1.  Load API key from .env (works no matter where uvicorn is started)
# ───────────────────────────────────────────────────────────────────────────────
dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path)

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

# ───────────────────────────────────────────────────────────────────────────────
# 2.  Configure the SDK — handle older versions that lack api_version= parameter
# ───────────────────────────────────────────────────────────────────────────────
try:
    # noinspection PyArgumentList
    genai.configure(api_key=API_KEY, api_version="v1")  # new SDKs (≥0.8)
except TypeError:
    # Fallback for older SDKs (<0.8) that don't accept api_version
    genai.configure(api_key=API_KEY)

# Use the full model path (as shown by list_models)
MODEL_ID = "models/gemini-1.5-flash"
MODEL = genai.GenerativeModel(MODEL_ID)

# ───────────────────────────────────────────────────────────────────────────────
# 3.  FastAPI application
# ───────────────────────────────────────────────────────────────────────────────
app = FastAPI(title="Gemini FastAPI Service", version="1.0.0")


class Prompt(BaseModel):
    prompt: str


def gemini_answer(prompt: str) -> str:
    """
    Call Gemini and return the plain-text response.
    Raises HTTP 500 on any SDK/runtime error.
    """
    try:
        response = MODEL.generate_content(prompt)
        return response.text
    except Exception as exc:
        # Print full traceback to the server console for debugging
        print("Gemini SDK Error:\n", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/generate")
async def generate_get(prompt: str = Query(..., description="Prompt for Gemini")):
    """
    Example:  GET /generate?prompt=Hello
    """
    return {"response": gemini_answer(prompt)}


@app.post("/generate")
async def generate_post(body: Prompt):
    """
    Example JSON body:
    { "prompt": "Summarise FastAPI in one sentence." }
    """
    return {"response": gemini_answer(body.prompt)}
