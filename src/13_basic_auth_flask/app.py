from flask import Flask
from flask_httpauth import HTTPBasicAuth

# create flask application
app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    return username == "aga" and password == "love1234"


# create HTTP routes for our application
@app.route("/")
@auth.login_required
def index():
    return "Index Page"


@app.route("/secret/")
@auth.login_required
def secret():
    return "secret data"


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
