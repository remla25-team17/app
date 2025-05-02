import os
import requests
from flask import jsonify, Flask
from requests.exceptions import RequestException, HTTPError

MODEL_SERVICE_URL = os.getenv('SENTIMENT_MODEL_ENDPOINT')

APP_SERVICE_VERSION = os.getenv('APP_SERVICE_VERSION')
MODEL_SERVICE_VERSION = os.getenv('MODEL_SERVICE_VERSION')

sentiment_api = Flask(__name__)

@sentiment_api.route('/api/sentiment', methods=['POST'])
def analyze_sentiment(input_text: str):
    """
        Analyze the sentiment of the provided input text by sending it to the model service.

        Args:
            input_text (str): The text for which sentiment analysis is to be performed.

        Returns:
            Response: A Flask JSON response with the sentiment result or an error message.
        """
    if len(input_text) == 0:
        return jsonify({'error': 'Input text cannot be empty.'}), 400

    try:
        response = requests.post(
            url=MODEL_SERVICE_URL,
            json={'text': input_text}
        )
        response.raise_for_status()
    except HTTPError as e:
        return jsonify({'error': f"Error in model service: {str(e)}"}), 500
    except RequestException as e:
        return jsonify({'error': f"Failed to connect to model service: {str(e)}"}), 503

    result = response.json()

    return jsonify({'sentiment': result}), 200

@sentiment_api.route('/api/version', methods=['GET'])
def get_version():
    return jsonify(
        {
            'app_service_version': APP_SERVICE_VERSION,
            'model_service_version': MODEL_SERVICE_VERSION
         }
    ), 200