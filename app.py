from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route("/")
def index():
    return "HELLO IT WORKS"
