from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
import config

# create flask application
app = Flask(__name__)


# create HTTP routes for our application
@app.route("/")
def index():
    return render_template("index.html", show_secret=False, top_secret_message=config.TOP_SECRET_MESSAGE)


@app.route("/add_comment/")
def add_comment():
    return render_template("add_comment.html")


@app.route("/secret/")
def secret():
    return render_template("index.html", show_secret=True)


@app.route("/comments/")
def comments():
    return render_template("comments.html", comments=config.COMMENTS)


@app.route("/submit_comment/", methods=['GET', 'POST'])
def submit_comment():
    if request.method == 'POST':
        user = request.form.get("user")
        comment = request.form.get("comment")
    else:
        user = request.args.get("user")
        comment = request.args.get("comment")

    data = {"user": user, "comment": comment}
    config.COMMENTS.append(data)
    return redirect("/comments/")


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
