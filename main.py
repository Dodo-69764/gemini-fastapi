import os

from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

app = FastAPI(title="Gemini FastAPI Microservice")


class Prompt(BaseModel):
    prompt: str


@app.get("/generate")
async def generate_get(prompt: str = Query(..., min_length=1)):
    try:
        response = model.generate_content(prompt)
        return {"response": response.text}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/generate")
async def generate_post(body: Prompt):
    try:
        response = model.generate_content(body.prompt)
        return {"response": response.text}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
