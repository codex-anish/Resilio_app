import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def speech_to_text(audio_bytes: bytes, mime_type: str):
    response = model.generate_content(
        [
            "Transcribe the following audio clearly into plain text only.",
            {
                "mime_type": mime_type,
                "data": audio_bytes
            }
        ]
    )
    return response.text
