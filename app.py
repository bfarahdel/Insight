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
        ent_len=3,
        echo_medical=echo_medical,
        med_entry=["d3e5b67c-061f-4977-9b3a-8d4027f80905", "6f276bf7-d203-4676-8813-df72f680ae8c", "1861a637-1e6e-43af-b7fd-2e87a67bb225"],
        med_name=["Heart", "Lungs (Exhale)", "Human Immunodeficiency Virus (HIV)"],
        echo_geo=echo_geo,
        geo_entry=["2c34c3ae-d390-4b7a-af82-706eb2e6103d", "4e2552af-6c7d-4670-bbbc-617b823b855b", "247a7845-f12b-4a75-9879-370af28f4aa1"],
        geo_name=["US Capitol","Buckingham Palace", "Great Wall of China"],
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )