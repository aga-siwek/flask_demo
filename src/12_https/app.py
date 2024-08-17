from flask import Flask
from flask import request
import base64

# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/")
def index():
    return "Index Page"


@app.route("/secret/")
def secret():
    if "Authorization" in request.headers.keys():
        login_data_encoded = request.headers["Authorization"].split()[1]
        login_data_decoded = base64.b64decode(login_data_encoded).decode("utf-8")
        user = login_data_decoded.split(":")[0]
        password = login_data_decoded.split(":")[1]

        # flask also parse this data for us automatically
        # user = request.authorization.parameters["username"]
        # password = request.authorization.parameters["password"]

        if user == "aga" and password == "love123":
            return "secret data"

    auth = {'WWW-Authenticate': 'Basic realm="MyApp"'}
    return "you don't have authorization", 401, auth


if __name__ == "__main__":
    # ssl_context adhoc is used to created local certyficate to enable https
    app.run(port=1234, host="0.0.0.0", ssl_context="adhoc")
