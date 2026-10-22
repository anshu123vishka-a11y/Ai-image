import os
from urllib.parse import urlparse

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl

app = FastAPI(
    title="Nexa Image Backend",
    description="Starter API for image-generation workflows and opening Canva.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your app's origins before production.
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

CANVA_HOME = "https://www.canva.com/"


class CanvaOpenRequest(BaseModel):
    image_url: HttpUrl | None = None


@app.get("/")
def root():
    return {
        "service": "Nexa Image Backend",
        "status": "running",
        "docs": "/docs",
        "note": "Canva website opening is supported; automatic image import is not configured.",
    }


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/canva/open")
def canva_open(payload: CanvaOpenRequest):
    """Return Canva's website URL. Does not claim to import the image automatically."""
    image_url = str(payload.image_url) if payload.image_url else None
    if image_url:
        host = (urlparse(image_url).hostname or "").lower()
        if not host:
            raise HTTPException(status_code=400, detail="Invalid image URL")

    return {
        "canva_url": CANVA_HOME,
        "image_url": image_url,
        "image_imported": False,
        "message": "Open Canva. Automatic image import requires a supported Canva integration.",
    }


@app.get("/canva/open-website")
def open_canva_website():
    return RedirectResponse(url=CANVA_HOME, status_code=307)
