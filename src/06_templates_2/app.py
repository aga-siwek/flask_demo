from flask import Flask
from flask import render_template
import config

# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/")
def index():
    return render_template("index.html", show_secret=False, top_secret_message=config.TOP_SECRET_MESSAGE)


@app.route("/secret/")
def secret():
    return render_template("index.html", show_secret=True)


@app.route("/comments/")
def comments():
    return render_template("comments.html", comments=config.COMMENTS)


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
