# Use a slim Python base image
FROM python:3.12-slim

# Set a working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source files into the container
COPY . /app/

# Expose default Flask port
EXPOSE 5000

# Run the Flask app
ENTRYPOINT ["python"]
CMD ["app.py"]