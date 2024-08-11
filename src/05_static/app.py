from flask import Flask
from flask import send_file
from flask import render_template
import config

# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/")
def index():
    return send_file("templates/index.html")


@app.route("/about/")
def about():
    return send_file("templates/about.html")


@app.route("/contact/")
def contact():
    # phone number is added to HTML template
    return render_template("contact.html", phone_number=config.PHONE_NUMBER)


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
