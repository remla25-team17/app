import os
from flask import Flask, render_template
from flasgger import Swagger
from lib_version import VersionUtil  
from src.sentiment_api import sentiment_api

app = Flask(__name__, template_folder="src")
app.register_blueprint(sentiment_api)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print(f"The lib-version used is {VersionUtil.get_version()}")
    port = int(os.getenv("PORT", 5000)) 
    host = os.getenv("HOST", "0.0.0.0")
    app.run(host=host, port=port)