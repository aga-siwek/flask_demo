from flask import Flask, render_template, request, redirect, session
import config

# create flask application
app = Flask(__name__)

users_pass = {
    "aga": {"password": "love123", "isAdmin": False},
    "pawel": {"password": "widelec", "isAdmin": True},
    "admin": {"password": "admin", "isAdmin": True},
}

# Set the secret key to some random bytes. Keep this really secret!

app.secret_key = b'xyz'


def is_admin(username):
    if username not in users_pass.keys():
        return False

    return users_pass[username]["isAdmin"]


# create HTTP routes for our application
@app.route("/")
def index():
    if "username" in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", wrong_login=False)
    if request.method == "POST":
        added_username = request.form["username"]
        added_password = request.form["password"]

        if added_username in users_pass.keys():
            if users_pass[added_username]["password"] == added_password:
                session["username"] = added_username
                return redirect("/")
        return render_template("login.html", wrong_login=True)


@app.route("/logout/")
def logout():
    # remove the username from the session if it's there

    session.pop("username", None)
    return redirect("/")


@app.route("/user/")
def user():
    if "username" in session:
        return f"Hi {session['username']}!"

    # check if user is logged (if cookie exist), if yes print username otherwise print "not logged in"

    return "not logged in"


@app.route("/admin/")
def admin():
    if "username" in session:
        if not is_admin(session["username"]):
            return "Access denied"

        return config.TOP_SECRET_MESSAGE
    return "Not logged in"


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
