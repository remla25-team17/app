import os
import requests
from flask import jsonify, Flask, request
from requests.exceptions import RequestException, HTTPError

MODEL_SERVICE_URL = os.getenv('MODEL_SERVICE_URL')
APP_SERVICE_VERSION = os.getenv('APP_SERVICE_VERSION', 'unknown')

if not MODEL_SERVICE_URL:
    raise EnvironmentError("MODEL_SERVICE_URL environment variable is not set.")

sentiment_api = Flask(__name__)

@sentiment_api.route('/api/v1/sentiment', methods=['POST'])
def analyze_sentiment():
    """
    Analyze the sentiment of the provided input text by sending it to the model service.

    Expects JSON request body: {"text": "<input_text>"}

    Returns:
        Response: A JSON response with the sentiment result or an error message.
    """
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            return jsonify({'error': 'Missing "text" field in JSON payload.'}), 400

        input_text: str = data['text']
        if not isinstance(input_text, str):
            return jsonify({'error': 'Input text must be a string.'}), 400
        if not input_text.strip():
            return jsonify({'error': 'Input text cannot be empty.'}), 400

    except ValueError:
        return jsonify({'error': 'Invalid JSON payload.'}), 400

    try:
        response = requests.post(
            url=MODEL_SERVICE_URL,
            json={'text': input_text}
        )
        response.raise_for_status()
        sentiment_prediction = response.json().get('sentiment')
    except HTTPError as e:
        return jsonify({'error': f"Error in model service: {str(e)}"}), 500
    except RequestException as e:
        return jsonify({'error': f"Failed to connect to model service: {str(e)}"}), 503

    return jsonify({'sentiment': sentiment_prediction}), 200

@sentiment_api.route('/api/v1/version', methods=['GET'])
def get_version():
    """
    Retrieve the version of the app and model service.

    Returns:
        Response: A JSON response with version information.
    """
    try:
        response = requests.get(f'{MODEL_SERVICE_URL}/api/version')
        response.raise_for_status()
        model_service_version = response.json().get('model_service_version', 'unknown')
    except HTTPError as e:
        return jsonify({'error': f"Error in model service: {str(e)}"}), 500
    except RequestException as e:
        return jsonify({'error': f"Failed to connect to model service: {str(e)}"}), 503

    return jsonify(
        {
            'app_service_version': APP_SERVICE_VERSION,
            'model_service_version': model_service_version
         }
    ), 200