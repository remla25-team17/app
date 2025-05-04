# Use a slim Python base image
FROM python:3.12-slim

# Set a working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files into the container
COPY . .

# Set environment variables
ARG APP_SERVICE_VERSION
ENV APP_SERVICE_VERSION=${APP_SERVICE_VERSION}

ENV MODEL_SERVICE_URL=""

# Expose default Flask port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "--app", "src/sentiment_api", "run"]
