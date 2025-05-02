FROM python:3.12-slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV MODEL_SERVICE_URL=""
CMD ["flask", "--app", "src/sentiment_api", "run"]