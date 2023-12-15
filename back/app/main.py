from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import shutil
from pathlib import Path

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(open(file_path, "rb"), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})
