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