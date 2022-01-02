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
    print(flask.Response())
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
    echo_am_key= os.getenv("echo_am")

    echo_medical = f"https://api.echo3D.co/webar?key={echo_medical_key}"
    echo_geo = f"https://api.echo3D.co/webar?key={echo_geo_key}"
    echo_am = f"https://api.echo3D.co/webar?key={echo_am_key}"

    echo_med_img=[
        "https://dl.dropboxusercontent.com/s/9tupiaa9nczexb6/Heart.png?dl=0",
        "https://dl.dropboxusercontent.com/s/jk7gt3fs4d2cw2y/Lungs.png?dl=0",
        "https://dl.dropboxusercontent.com/s/0zt1c7rlvq77x7i/HIV.png?dl=0",
    ]

    echo_geo_img=[
        "https://dl.dropboxusercontent.com/s/mlfh3ojl4oo94dh/Everest.png?dl=0",
        "https://dl.dropboxusercontent.com/s/zdpdvlbhxqyqpzy/Buckingham.png?dl=0",
        "https://dl.dropboxusercontent.com/s/q17edkaw0ivqm1w/Great_Wall.png?dl=0",
    ]

    echo_am_img=[
        "https://dl.dropboxusercontent.com/s/gyy0zx4iu53yq6k/Arctic_Fox.png?dl=0",
        "https://dl.dropboxusercontent.com/s/5vjl865xx7bckw9/Goat.png?dl=0",
        "https://dl.dropboxusercontent.com/s/o34gxxldaxjqvkm/Ferret.png?dl=0",
    ]

    return flask.render_template(
        "ar_models.html",
        ent_len=3,
        echo_medical=echo_medical,
        med_entry=["d3e5b67c-061f-4977-9b3a-8d4027f80905", "6f276bf7-d203-4676-8813-df72f680ae8c", "1861a637-1e6e-43af-b7fd-2e87a67bb225"],
        med_name=["Heart", "Lungs (Exhale)", "Human Immunodeficiency Virus (HIV)"],
        echo_med_img=echo_med_img,
        echo_geo=echo_geo,
        geo_entry=["147f240c-cd1c-4578-b6d4-c84309285d1e", "4e2552af-6c7d-4670-bbbc-617b823b855b", "247a7845-f12b-4a75-9879-370af28f4aa1"],
        geo_name=["Mount Everest","Buckingham Palace", "Great Wall of China"],
        echo_geo_img=echo_geo_img,
        echo_am=echo_am,
        am_entry=["9d434bf3-e0a7-4d1d-8ded-3150e41c52a1", "0990d8df-2cef-46f3-bafc-98c26988a941", "01ea25ef-38d9-45bc-96ff-f35318bf90c9"],
        am_name=["Arctic Fox", "Goat", "Ferret"],
        echo_am_img=echo_am_img,
    )

if __name__ == "__main__":
    app.run(
        host=os.getenv("IP", "0.0.0.0"),
        port=os.getenv("PORT", "8088"),
    )