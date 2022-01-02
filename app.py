import os
from dotenv import find_dotenv, load_dotenv
import flask
from flask import request
from symbl_api import symbl_api
from flask_ckeditor import CKEditor

app = flask.Flask(__name__)
app.secret_key = os.getenv("flask_secret")
ckeditor = CKEditor(app)

load_dotenv(find_dotenv())

@app.route("/", methods=["POST", "GET"])
def main():

    return flask.render_template(
        "index.html",
    )

@app.route("/notes", methods=["POST", "GET"])
def notes_page():
    msg = []
    if request.method=="POST":
        f = request.files['file']
        f.save(f.filename)
        msg = symbl_api().audio_text(path=f.filename)
        f.close()
        os.remove(f.filename)

    return flask.render_template(
        "notes.html",
        msg="\n".join(msg),
    )

@app.route("/models", methods=["POST","GET"])
def echo_models():
    echo_medical_key = os.getenv("echo_medical")
    echo_geo_key= os.getenv("echo_geo")

    echo_medical = f"https://api.echo3D.co/webar?key={echo_medical_key}"
    echo_geo = f"https://api.echo3D.co/webar?key={echo_geo_key}"

    return flask.render_template(
        "ar_models.html",
        echo_medical=echo_medical,
        echo_geo=echo_geo,
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
        debug=True,
    )