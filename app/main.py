from fastapi import FastAPI, UploadFile, File
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the AI Voice Assistant API!"}

@app.post("/speech-to-text/")
async def speech_to_text(file: UploadFile = File(...)):
    """
    Converts an uploaded audio file to text using Whisper.
    """
    try:
        # Save the uploaded file temporarily
        with open(file.filename, "wb") as audio_file:
            audio_file.write(await file.read())

        # Use Whisper for transcription
        result = subprocess.run(
            ["whisper", file.filename, "--output_format", "txt"],
            capture_output=True,
            text=True
        )

        transcription = result.stdout
        return {"transcription": transcription}

    except Exception as e:
        return {"error": str(e)}
