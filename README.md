# FastAPI Log Generator

This project is a FastAPI application that provides two endpoints for generating logs and errors.

## Endpoints

- `/generate-log`: Generates 5 logs including info, debug, and warning levels.
- `/generate-error`: Generates a Python exception, logs it, and re-raises it.

## Development

To run the project locally:

1. Install dependencies: `pip install -r requirements.txt`
2. Run the server: `DEV_MODE=true python main.py`

The server will start at `http://localhost:8000`.

## Docker

To build and run the Docker image:

```
docker build -t fastapi-log-generator .
docker run -p 8000:8000 fastapi-log-generator
```

## Gitpod

Click the button below to start a new development environment:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/yourusername/your-repo-name)

## Environment Variables

- `DEV_MODE`: Set to `true` for local development mode.

## API Documentation

FastAPI automatically generates OpenAPI (Swagger) documentation. Access it at `/docs` when the server is running.
