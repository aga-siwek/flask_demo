from flask import Flask, render_template, request, redirect
import os
from pathlib import Path

# create flask application
app = Flask(__name__)


def save_form_data_to_file(form_data):
    # check if "out" folder exist, if not create
    if not os.path.exists("out"):
        os.mkdir("out")

    # save form data to file user_name.txt in "out" folder
    file_name = form_data.get("name").replace(" ", "_").lower()

    with open(Path("out", f"{file_name}.txt"), "w") as file:
        file.write(form_data.get("name") + "\n")
        file.write(form_data.get("email") + "\n")
        file.write(form_data.get("number") + "\n")
        file.write(form_data.get("recommend") + "\n")
        file.write(form_data.get("help") + "\n")
        file.write(", ".join(form_data.getlist("favorite_project")) + "\n")
        file.write(form_data.get("message"))


# create HTTP routes for our application
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        save_form_data_to_file(request.form)
        return redirect("/thank_you/")


@app.route("/thank_you/")
def thank_you():
    return render_template("thank_you.html")


if __name__ == "__main__":
    # start our application
    app.run(port=1234, host="0.0.0.0")
