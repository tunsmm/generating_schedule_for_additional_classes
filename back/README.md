# Backend directory

This is a basic FastAPI application that allows you to upload files and download them.

## Setup

### manual setup

1. Install the required dependencies using the following command:

```bash
pip install -r requirements.txt
```

2. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

### via Docker

1. From this directory run the following command:

```bash
docker-compose up -d 
```

In both cases this will start the server at http://127.0.0.1:8000.


## Configuration

You can configurate different variables in `back/app/config.py`
- UPLOAD_DIR - all uploaded files is placed here
- GENERATED_SCHEDULE_DIR - - all generated schedule files
- WEEKDAYS_COUNT - how many week days in your week
- CLASSES_COUNT - how many classes or pairs for each day
- MAX_GROUP_CAPACITY - how many people per additional group
- GENERATED_FILE_NAME - name of file with generated schedule


## Usage

**Upload File**

To upload a file, use the `/uploadfile/` endpoint. Refer to the Swagger documentation at http://127.0.0.1:8000/docs and make a `POST` request to `/uploadfile/`.

It will create `uploads` directory in your system and will store all files there.

**Download File**
To download a file, use the `/downloadfile/{filename}` endpoint. Replace `filename` with the actual filename you want to download. Access the Swagger documentation or http://127.0.0.1:8000/redoc for details.


## Important Notes

- Uploaded files are stored in the `uploads` directory.
- Generated schedule  files are stored in the `generated_schedule` directory.
- Ensure the directory exists or the program will create it automatically.
- Customize the application based on your specific requirements.