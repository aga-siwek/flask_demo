from flask import Flask
from flask import send_file

app = Flask(__name__)


@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/about/")
def about():
    return send_file("templates/about.html")


@app.route("/contact/")
def contact():
    return send_file("templates/contact.html")


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
