from dotenv import load_dotenv
from groq import Groq
import tempfile
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def transcribe_audio(audio_bytes):

    with tempfile.NamedTemporaryFile(
        suffix=".webm",
        delete=False
    ) as temp_audio:

        temp_audio.write(audio_bytes)

        temp_path = temp_audio.name

    try:

        with open(temp_path, "rb") as file:

            transcription = client.audio.transcriptions.create(
                file=(temp_path, file.read()),
                model="whisper-large-v3"
            )

        return transcription.text

    finally:

        if os.path.exists(temp_path):
            os.remove(temp_path)