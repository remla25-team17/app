# App Service

## Features

* REST API for sentiment analysis, which query the model-service for predicting the sentiment of the input text
* Sentiment correction feedback endpoint
* Version endpoint for app and model service
* User interface for submitting reviews

## Environment Variables

* `MODEL_SERVICE_URL`: URL of the model-service
* `APP_SERVICE_VERSION`: app-service version

## API Endpoints

### `POST /api/v1/sentiment`

Analyze sentiment of the input text.

**Request Body**:

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

### `POST /api/v1/correct-prediction`

Accepts correction feedback from the user. (Currently not stored)

**Request Body**:

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

### `GET /api/v1/version`

Returns version information for both app and model service.

**Response**:

```json
{
  "app_service_version": "1.0.0",
  "model_service_version": "2.1.0"
}
```

## Frontend Overview

* Users can submit their review in a text area.
* On submission, the review is sent to `/api/v1/sentiment`.
* Sentiment result is displayed.
* Users can confirm or correct the sentiment, and corrections are posted to `/api/v1/correct-prediction`.


## Running the Application

### Prerequisites

* Python (version 3.12 or higher)
* pip (usually included with Python)
* Access to the model-service (ensure `MODEL_SERVICE_URL` is correctly configured)

### Setup and Running

**Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

**Configure Environment Variables**:
   Create a `.env` file in the root directory and add the following:
   ```bash
   MODEL_SERVICE_URL=<model-service-url>
   APP_SERVICE_VERSION=<app-service-version>
   ```
   Replace `<model-service-url>` with the actual URL of the model-service and `<app-service-version>` with the desired version (e.g., `1.0.0`).

**Start the Application**:
   ```bash
   flask --app src/sentiment_api run
   ```
   The application will run on `http://127.0.0.1:5000/` by default (or the port specified in your configuration).

   Alternatively, you can run the app directly with:
   ```bash
   python src/app.py
   ```

**Access the Application**:
   - Open a browser and navigate to `http://localhost:5000` to use the frontend interface.
   - Use tools like Postman or curl to interact with the API endpoints (e.g., `POST /api/v1/sentiment`).

This README was partly written with the help of generative AI.