import cv2
import numpy as np

def analyze_image(image_bytes: bytes):
    """
    Analyzes emergency image and detects incident type
    """

    # 1️⃣ Convert bytes → OpenCV image
    np_img = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    if img is None:
        return {
            "incident": "invalid_image",
            "confidence": 0.0
        }

    height, width, _ = img.shape

    # 2️⃣ Simple rule-based AI logic (demo / exam)
    if height > 500 and width > 500:
        incident = "accident"
        confidence = 0.82
    else:
        incident = "unknown"
        confidence = 0.45

    # 3️⃣ Return AI result
    return {
        "incident": incident,
        "confidence": confidence
    }
