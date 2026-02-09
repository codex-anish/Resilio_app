import whisper
import tempfile
import os

# Load Whisper model once (important for performance)
model = whisper.load_model("base")

# Keywords for severity detection
CRITICAL_KEYWORDS = [
    "fire",
    "accident",
    "bleeding",
    "unconscious",
    "help",
    "emergency",
    "injured",
    "collapse"
]

def analyze_audio(audio_bytes: bytes):
    """
    Converts voice to text and detects severity
    """

    # 1️⃣ Save audio temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        temp_audio.write(audio_bytes)
        audio_path = temp_audio.name

    # 2️⃣ Speech to Text
    result = model.transcribe(audio_path)
    text = result["text"].lower()

    # 3️⃣ Severity detection (rule-based, simple & exam-friendly)
    severity = "minor"
    for word in CRITICAL_KEYWORDS:
        if word in text:
            severity = "critical"
            break

    # 4️⃣ Cleanup temp file
    os.remove(audio_path)

    # 5️⃣ Return AI result
    return {
        "transcribed_text": text,
        "detected_severity": severity
    }
