from flask import Flask
import platform

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! This is Python " + platform.python_version()