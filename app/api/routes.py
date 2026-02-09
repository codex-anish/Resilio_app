from fastapi import APIRouter, UploadFile, File
from app.services.image_ai import analyze_image
from app.services.audio_ai import analyze_audio

router = APIRouter()

@router.post("/ai/emergency")
async def ai_emergency(
    image: UploadFile = File(...),
    audio: UploadFile = File(None)
):
    # 1️⃣ Read image
    image_bytes = await image.read()
    image_result = analyze_image(image_bytes)

    # 2️⃣ Read & analyze audio (if provided)
    audio_result = None
    if audio:
        audio_bytes = await audio.read()
        audio_result = analyze_audio(audio_bytes)


    # 4️⃣ Return AI result
    return {
        "status": "AI analysis completed",
        "image_analysis": image_result,
        "audio_analysis": audio_result
    }
