from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!!!!"


@app.route("/about/")
def about():
    return "Hi, My name is Pawel!"


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
