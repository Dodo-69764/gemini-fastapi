import os

from dotenv import load_dotenv


if not api_key:




class Prompt(BaseModel):
    prompt: str


    try:
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


async def generate_post(body: Prompt):
