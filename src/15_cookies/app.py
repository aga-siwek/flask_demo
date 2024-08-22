from flask import Flask, request, make_response
import datetime


# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/", methods=['GET', 'POST'])
def index():
    return "index"


@app.route("/set_cookie_1/")
def set_cookie_1():
    # cookie without expire
    response_data = make_response("set cookie 1")
    response_data.set_cookie("cookie1","value1")
    return response_data


@app.route("/set_cookie_2/")
def set_cookie_2():
    # cookie with expire property are saved after browser restart
    response_data = make_response("set cookie 2")
    response_data.set_cookie("cookie2", "value2", expires=datetime.datetime.now() + datetime.timedelta(days=1))

    return response_data


@app.route("/get_cookies/")
def get_cookies():
    return f"cookie1 = {request.cookies.get('cookie1')}, cookie2 = {request.cookies.get('cookie2')}"


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
