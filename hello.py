from flask import Flask
import platform

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello! This is Python!"
    # return "Hello! This is Python! " + platform.python_version()