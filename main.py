from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from utils.generate_video import generate_reel
import uuid

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("static/index.html", "r") as f:
        return HTMLResponse(content=f.read())

@app.post("/generate", response_class=FileResponse)
async def generate(prompt: str = Form(...)):
    filename = f"static/{uuid.uuid4().hex}.mp4"
    generate_reel(prompt, filename)
    return FileResponse(filename, media_type="video/mp4", filename="generated_reel.mp4")
