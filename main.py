from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(title="My Voice AI")

@app.get("/")
def home():
    return FileResponse(Path(_file_).parent / "index.html")
