from flask import Flask, render_template

import sentiment_api

app = Flask(__name__, template_folder="src")
app.register_blueprint(sentiment_api)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)