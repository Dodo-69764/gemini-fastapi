<<<<<<< HEAD
ï»¿FROM python:3.12-slim

WORKDIR /app

=======
FROM python:3.11-slim

WORKDIR /app
>>>>>>> 8e46334 (Initial Gemini FastAPI microservice)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

<<<<<<< HEAD
ENV GEMINI_API_KEY=\

EXPOSE 8000

=======
# You’ll pass the key at runtime:  -e GEMINI_API_KEY=xxx
ENV GEMINI_API_KEY=""

EXPOSE 8000
>>>>>>> 8e46334 (Initial Gemini FastAPI microservice)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
