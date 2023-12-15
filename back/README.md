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

This will start the server at http://127.0.0.1:8000.

## Usage

**Upload File**

To upload a file, use the `/uploadfile/` endpoint. Refer to the Swagger documentation at http://127.0.0.1:8000/docs and make a `POST` request to `/uploadfile/`.

**Download File**
To download a file, use the `/downloadfile/{filename}` endpoint. Replace `filename` with the actual filename you want to download. Access the Swagger documentation or http://127.0.0.1:8000/redoc for details.


## Important Notes

- Uploaded files are stored in the `uploads` directory.
- Ensure the directory exists or create it manually.
- Customize the application based on your specific requirements.