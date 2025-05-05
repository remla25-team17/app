from logging import log
from flask import Flask, render_template
from lib_version import VersionUtil  
import sentiment_api

app = Flask(__name__, template_folder="src")
app.register_blueprint(sentiment_api)

@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    print(f"The lib-version used is {VersionUtil.get_version()}")
    app.run(debug=True)