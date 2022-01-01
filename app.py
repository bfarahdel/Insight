import os
from dotenv import find_dotenv, load_dotenv
import flask
from flask import request, redirect, flash
from symbl_api import symbl_api

app = flask.Flask(__name__)
app.secret_key = os.getenv("flask_secret")

load_dotenv(find_dotenv())

@app.route("/", methods=["POST", "GET"])
def main():
    msg = []
    if request.method=="POST":
        f = request.files['file']
        f.save(f.filename)
        msg = symbl_api().audio_text(path=f.filename)
        f.close()
        os.remove(f.filename)

    return flask.render_template(
        "notes.html",
        msg=msg,
    )


if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )