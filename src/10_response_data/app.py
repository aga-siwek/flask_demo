from flask import Flask
from flask import render_template
from flask import make_response

# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/")
def index():
    # if function returns string response type is set to text/html and status to 200
    return "Index Page"


@app.route("/template")
def template():
    # render_template returns a string so same rules as above
    html_template = render_template("index.html")
    print(type(html_template))
    return html_template


@app.route("/my_list/")
def my_list():
    # if function returns a list a json response is created
    data = [True, 1, "text", [2, 3, "hello"]]

    return data


@app.route("/my_dict/")
def my_dict():
    # if function returns a dict a json response is created
    data = {
        "data": [10, 2, 15],
        "name": "Pawel",
        "age": 12
    }
    return data


@app.route("/status_code/")
def status_code():
    # if function return tuple with int as 2nd element, this int will be used as status code
    return "You need to log in", 401


@app.route("/headers/")
def headers():
    # if function return tuple with dictionary as 2nd element, this int will be used as headers
    headers_data = {
        "day": "Monday",
        "age": 17
    }
    return "test", headers_data


@app.route("/headers_code/")
def headers_code():
    # if function returns tuple with 3 elements, 2nd element is status code and 3rd it headers
    headers_data = {
        "day": "Saturday",
        "age": 33
    }

    return "body", 401, headers_data


@app.route("/response/")
def response():
    # we can create response object with make_response function and return it
    response_data = make_response("this is some text in body")
    response_data.status_code = 401
    response_data.headers["day"] = "Saturday"
    response_data.headers["age"] = "33"

    return response_data


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
