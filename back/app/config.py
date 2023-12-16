from pathlib import Path

# Directory to store uploaded files
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)
Path("uploads/schedules").mkdir(exist_ok=True)
Path("uploads/studentsGroups").mkdir(exist_ok=True)

# Directory to store result of generating schedule
GENERATED_SCHEDULE_DIR = Path("generated_schedule")
GENERATED_SCHEDULE_DIR.mkdir(exist_ok=True)
