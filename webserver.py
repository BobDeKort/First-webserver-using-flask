from flask import Flask
from flask import request
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/hello")
def second():
    return "Hello, how are you?"


@app.route("/pets", methods=["POST"])
def pets():
    result = json.dumps(request.json)
    return(result)


if __name__ == "__main__":
    app.run()
