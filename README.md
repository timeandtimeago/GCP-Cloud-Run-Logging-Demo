# FastAPI Log Generator

This project is a FastAPI application that provides endpoints for generating logs and errors. It's designed to demonstrate logging capabilities and error handling in a FastAPI environment.

## Features

- Two endpoints:
  - `/generate-log`: Generates 5 logs including info, debug, and warning levels.
  - `/generate-error`: Generates a Python exception, logs it, and re-raises it.
- Configurable development mode
- Docker support for production deployment
- Gitpod configuration for easy development setup
- Google Cloud CI/CD pipeline ready

## Prerequisites

- Python 3.9+
- Docker (for production deployment)
- Gitpod (for cloud development environment)

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and set `DEV_MODE=true` for local development.

5. Run the FastAPI server:
   ```
   python main.py
   ```

The server will start at `http://localhost:8000`.

## Docker Deployment

1. Build the Docker image:
   ```
   docker build -t fastapi-log-generator .
   ```

2. Run the Docker container:
   ```
   docker run -p 8000:8000 fastapi-log-generator
   ```

## Gitpod Development

Click the button below to start a new development environment:

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/yourusername/your-repo-name)

## Google Cloud CI/CD

This project includes a `cloudbuild.yaml` file for setting up a CI/CD pipeline with Google Cloud Build. The pipeline will:

1. Build the Docker image
2. Push the image to Google Cloud Artifact Registry
3. Deploy the image to Google Cloud Run

To use this pipeline:

1. Set up a Google Cloud project with Cloud Build, Artifact Registry, and Cloud Run enabled.
2. Connect your GitHub repository to Cloud Build.
3. Create a trigger that uses the `cloudbuild.yaml` file.

## API Documentation

FastAPI automatically generates OpenAPI (Swagger) documentation. Access it at `/docs` when the server is running.

## Environment Variables

- `DEV_MODE`: Set to `true` for local development mode. This enables debug logging and other development features.

## Project Structure
