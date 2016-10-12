from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def second():
    return "Hello, how are you?"


@app.route("/pets/<jsonData>", methods=["GET", "POST"])
def pets(jsonData):
    if request.method == "POST":
        return jsonData
    else:
        return "no data"


if __name__ == "__main__":
    app.run()
