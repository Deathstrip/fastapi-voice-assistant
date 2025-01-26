# FastAPI Voice Assistant

This is a FastAPI-based backend for an AI-powered voice assistant. It includes:
- Speech-to-Text conversion using Whisper.
- Easy deployment on Render.

## Endpoints
- `GET /`: Root endpoint.
- `POST /speech-to-text/`: Upload an audio file to get the text transcription.

## Setup and Deployment
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the server locally with `uvicorn app.main:app --reload`.
