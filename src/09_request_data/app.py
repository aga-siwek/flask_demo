from flask import Flask
from flask import render_template
from flask import request
import config
import utils

# create flask application
app = Flask(__name__)




# create HTTP routes for our application
@app.route("/")
def index():
    return render_template("index.html", show_secret=False, top_secret_message=config.TOP_SECRET_MESSAGE)


@app.route("/request_data/", methods=['GET', 'POST'])
def request_data():
    request.get_data()

    return render_template(
        "request_data.html",
        method=request.method,
        args=request.args,
        host_url=request.host_url,
        url=request.url,
        url_rule=request.url_rule,
        url_root=request.url_root,
        url_base=request.base_url,
        headers=request.headers,
        form=request.form,
        values=request.values,
        body=request.data,
        ip_visitor=request.remote_addr,

    )


@app.route("/request_data_new/", methods=['GET', 'POST'])
def request_data_new():
    request.get_data()

    return render_template(
        "request_data_new.html",
        method=request.method,
        args=utils.dict_to_indexed_list(request.args),
        host_url=request.host_url,
        url=request.url,
        url_rule=request.url_rule,
        url_root=request.url_root,
        url_base=request.base_url,
        headers=request.headers,
        form=request.form,
        values=request.values,
        body=request.data.decode(),
        ip_visitor=request.remote_addr,

    )


if __name__ == "__main__":
    app.run(port=1234, host="0.0.0.0")
