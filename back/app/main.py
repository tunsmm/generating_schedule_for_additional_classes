import shutil

from config import GENERATED_SCHEDULE_DIR, UPLOAD_DIR

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}

@app.get("/generate_schedule/")
async def generate_schedule():
    filename = 'stub_file.txt'
    file_path = GENERATED_SCHEDULE_DIR / filename

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(open(file_path, "rb"), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})
