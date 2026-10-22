# AI Image Backend (starter)

FastAPI starter backend for the AI image app.

## Endpoints
- GET / — service information
- GET /health — health check
- POST /canva/open — returns Canva website URL and optional image URL
- GET /canva/open-website — redirects to Canva

## Important
This starter only opens Canva's website. It does NOT automatically import an image into a Canva design. Automatic import requires a supported Canva integration and authorization flow. Image-generation APIs are not connected yet.

## Deploy on Render
This repository includes render.yaml. In Render choose New → Blueprint and connect this repository, or create a Web Service with:
- Build command: pip install -r requirements.txt
- Start command: uvicorn main:app --host 0.0.0.0 --port $PORT

After deployment, open /docs to test the API.

## Test
POST /canva/open with JSON:
{
  "image_url": "https://example.com/generated-image.png"
}

Before production, restrict CORS, add authentication/rate limits, and connect secure image storage and generation providers.
