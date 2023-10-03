"""This is the main file for the flask app. """
from flask import Flask, render_template, request, send_file
import time
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    This function returns the index.html page
    :return:
    """
    return render_template("index.html", title="Hello")

@app.route("/image")
def image():
    """
    This function returns a random image from the static folder
    :return:
    """
    # get the image number from the url
    num = request.args.get("img")
    if num not in ["1", "2", "3"]:
        return "Invalid image number", 400

    # Return a random image inside the static folder and the image number in the header as X-Ece252-Fragment: <num>
    random_num = random.randint(0,49)
    path = f"static/image_{num}/image-{random_num}.png"
    response = send_file(path, mimetype="image/png")
    response.headers["X-Ece252-Fragment"] = num
    return response


