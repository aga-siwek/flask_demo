from flask import Flask, render_template, request, redirect, make_response
import config

# create flask application
app = Flask(__name__)

users_pass = {
    "aga": {"password": "love123", "isAdmin": False},
    "pawel": {"password": "widelec", "isAdmin": True},
    "admin": {"password": "admin", "isAdmin": True},
}


def get_current_user():
    # check the user in cookies, return user name or none.
    if request.cookies.get("user") is None:
        return None
    if request.cookies.get("user") == "":
        return None

    return request.cookies.get("user")


def is_admin(username):
    if username not in users_pass.keys():
        return False

    return users_pass[username]["isAdmin"]


# create HTTP routes for our application
@app.route("/")
def index():
    return "index"


@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        username = request.form.get("user")
        password = request.form.get("password")

        if username in users_pass.keys():
            if password == users_pass[username]["password"]:
                # if user and password correct, save current user to cookies and redirect to /user/
                response_data = make_response(redirect("/user/"))
                response_data.set_cookie("user", username)
                return response_data

        # if user and password not correct, redirect to /invalid_user/
        return redirect("/invalid_user/")


@app.route("/invalid_user/")
def invalid_user():
    return "invalid username or password"


@app.route("/logout/")
def logout():
    response_data = make_response("logged out")
    response_data.set_cookie("user", "")
    return response_data


@app.route("/user/")
def user():
    # check if user is logged (if cookie exist), if yes print username otherwise print "not logged in"
    current_user = get_current_user()

    if current_user is not None:
        return f"Hi {current_user}!"

    return "not logged in"


@app.route("/admin/")
def admin():
    current_user = get_current_user()

    if current_user is None:
        return "Not logged in"

    if not is_admin(current_user):
        return "Access denied"

    return config.TOP_SECRET_MESSAGE


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
