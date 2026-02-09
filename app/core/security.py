from fastapi import FastAPI
from api.routes import router

# Create FastAPI app
app = FastAPI(
    title="Resilio AI Backend",
    description="AI service for image and voice analysis in emergency response",
    version="1.0.0"
)

# Register routes
app.include_router(router)

# Health check (optional but useful)
@app.get("/")
def health_check():
    return {"status": "Resilio AI backend is running"}
