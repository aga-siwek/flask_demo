from flask import Flask

app = Flask(__name__)

WEB_PAGE_CONTENT = """
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>Flask App</h1>
    <p>Welcome to my application</p>
</body>
</html>

"""


@app.route("/")
def index():
    return WEB_PAGE_CONTENT


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
