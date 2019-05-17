from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/post")
def post():
    return "this is where the post will be"


@app.route("/signin")
def signin():
    return render_template("signin.html")
