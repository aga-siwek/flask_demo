from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from pathlib import Path
import config

# create flask application
app = Flask(__name__)


def read_comments_from_db():
    database_path = Path.cwd() / Path("database", "db.txt")
    file = open(database_path, "r")
    comments_user = file.read().split("\n")
    comments_dictionary = []

    for i, item in enumerate(comments_user):
        if i % 2 == 0:
            one_comments = {"user": item, "comment": comments_user[i + 1]}
            comments_dictionary.append(one_comments)

    return comments_dictionary


def add_comment_to_db(user, comment):
    database_path = Path.cwd() / Path("database", "db.txt")
    file = open(database_path, "a")
    file.write(f"\n{user}")
    file.write(f"\n{comment}")
    file.close()


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
    return render_template("comments.html", comments=read_comments_from_db())


@app.route("/submit_comment/", methods=['GET', 'POST'])
def submit_comment():
    if request.method == 'POST':
        user = request.form.get("user")
        comment = request.form.get("comment")
    else:
        user = request.args.get("user")
        comment = request.args.get("comment")

    # data = {"user": user, "comment": comment}
    # config.COMMENTS.append(data)
        add_comment_to_db(user, comment)
    return redirect("/comments/")


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
