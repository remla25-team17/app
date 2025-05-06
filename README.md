# App Service

A lightweight Flask application that offers a RESTful API and frontend interface for **sentiment analysis**. It connects with a model-service to analyze user-submitted text and supports feedback collection for prediction corrections.

---

## 📚 Table of Contents

- [🚀 Features](#-features)
- [🛠 Requirements](#-requirements)
- [🔧 Local Setup](#-local-setup)
- [📡 API Endpoints](#-api-endpoints)
- [🖥 Frontend](#-frontend)
- [📦 Running with Docker](#-running-with-docker)
- [📜 Resources](#-resources)

---

## 🚀 Features

- **API Endpoints**:
  - `POST /api/v1/sentiment`: Analyze sentiment of input text via model-service.
  - `POST /api/v1/correct-prediction`: Submit correction feedback for predicted sentiment.
  - `GET /api/v1/version`: View current versions of app and model service.
- **Swagger UI**: Built-in Swagger documentation for easy API exploration.
- **Containerized**: Fully containerized with Docker for consistent deployment.
- **CI/CD**:
  - Automated builds and Docker image pushes to **GitHub Container Registry (GHCR)**.
  - **Semantic versioning** with GitVersion.
---

## 🛠 Requirements

- Python 3.8+
- pip
- Access to a running model-service instance (or container)

---

## 🔧 Local Setup

1️⃣ **Clone the repository**:

```bash
git clone git@github.com:remla25-team17/app.git
cd app
````

2️⃣ **Install dependencies**:

```bash
pip install -r requirements.txt
```

3️⃣ **Configure environment variables**:

Create a `.env` file in the root directory with the following:

```env
MODEL_SERVICE_URL=<model-service-url>
APP_SERVICE_VERSION=<app-version>
```

4️⃣ **Start the application**:

```bash
flask run
```

Or run directly:

```bash
python app.py
```

📍 The app will be available at:
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📡 API Endpoints

### `POST /api/v1/sentiment`

Analyze sentiment of the given input text.

**Request**:

```json
{
  "text": "The food was good"
}
```

**Response**:

```json
{
  "sentiment": "1"
}
```

---

### `POST /api/v1/correct-prediction`

Submit a corrected prediction. (Note: Currently not persisted)

**Request**:

```json
{
  "text": "The food was good",
  "original_prediction": "0",
  "corrected_prediction": "1"
}
```

**Response**:

```json
{
  "message": "Your correction has been processed."
}
```

---

### `GET /api/v1/version`

Returns version details of the app and connected model-service.

**Response**:

```json
{
  "app_service_version": "1.0.0",
  "model_service_version": "2.1.0"
}
```

---

## 🖥 Frontend

* Users can enter a text review into a form.
* The input is sent to `/api/v1/sentiment` for analysis.
* Results are displayed instantly.
* Optionally, users can correct the sentiment and send feedback to `/api/v1/correct-prediction`.

---

## 📦 Running with Docker

Docker enables you to package the application and run it in a consistent environment across platforms.

1️⃣ **Build the Docker image**:

```bash
docker build -t app-service .
```

- `docker build`: This command tells Docker to create an image from the Dockerfile in the current directory.
- `-t sentiment-service`: Tags the image with the name `sentiment-service` for easier reference.
- `.`: Specifies the build context (current directory).

2️⃣ **Run the container**:

```bash
docker run -p 8080:8080 --env-file .env app-service
```

- `docker run`: Starts a new container from the `app-service` image.
- `-p 8081:8081`: Maps port 8080 on your local machine to port 8080 inside the container, making the API accessible at [http://localhost:8080](http://localhost:8080).
- `--env-file=.env`: Loads environment variables from the `.env` file.
- `app-service`: Specifies the image to run.

---
## [⚙️ GitHub Actions & CI/CD](#-github-actions--cicd)

- **Build & Push**:

  - Every push to `main` or `develop/**` triggers GitHub Actions.
  - The Docker image is built and pushed to:  
    `ghcr.io/remla25-team17/app:<version>`

- **GitHub App Authentication**:

  - For this project, we use a **GitHub App** to handle authentication in our CI/CD pipeline. This provides:
    - **Better security**: Fine-grained control over permissions.
    - **Reliable access**: Works across repositories or teams in the same organization.
    - **Clear traceability**: Actions are marked as being done by the GitHub App.

- **Versioning**:
  - **GitVersion** is used for semantic versioning. It analyzes the Git history and branch structure to generate a **semantic version number** (SemVer) automatically.
  - Commit messages can specify `#major`, `#minor`, or `#patch` to control version increments.
  - Examples:
    - Merges to `main` bump a stable version (e.g., `1.0.0`).
    - Builds from feature branches or pre-release branches (e.g., `develop`) are marked as **pre-releases** (e.g., `1.1.0-canary.5`).

---


## 📜 Resources

* [Flask Documentation](https://flask.palletsprojects.com/)
* [REST API Design](https://restfulapi.net/)
* [Semantic Versioning](https://semver.org/)
* [Docker Documentation](https://docs.docker.com/)
* [Swagger UI](https://swagger.io/tools/swagger-ui/)
