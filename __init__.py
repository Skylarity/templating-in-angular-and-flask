from flask import Flask, session, send_file, render_template

app = Flask(__name__)


@app.route("/")
def index():
    session["username"] = "Skylarity"
    return send_file("templates/index.html")


@app.route("/views/<string:page_name>")
def view(page_name):
    return render_template("views/%s.html" % page_name)


app.secret_key = '\x10CvN@\x1e\xf7\xf1\xa1\x9aOa\xfcu\xb4[\xdf\x80X\xfc\xa4\x91\xd4G'


if __name__ == "__main__":
    app.run(host="0.0.0.0")
