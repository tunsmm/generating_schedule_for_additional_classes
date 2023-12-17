import shutil

from config import UPLOAD_DIR

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from schedule import get_generated_schedule_name

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/uploadfile/schedules")
async def create_upload_schedule_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = UPLOAD_DIR / "schedules" / file.filename
    print(file_path)
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}


@app.post("/uploadfile/studentsGroups")
async def create_upload_student_file(file: UploadFile = File(...)):
    # Save the uploaded file
    file_path = UPLOAD_DIR / "studentsGroups" / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}


@app.get("/generate_schedule/")
async def get_generated_schedule():
    file_path = get_generated_schedule_name()

    if not file_path.exists():
        raise HTTPException(
            status_code=404, 
            detail=f"File with name {file_path.split('/')[-1]} is not found",
        )

    return StreamingResponse(open(file_path, "rb"), media_type="application/octet-stream", headers={"Content-Disposition": f"attachment; filename={filename}"})
