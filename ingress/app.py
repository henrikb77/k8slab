import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def root():
    return f"App v{os.getenv('VERSION')} running\n"

@app.route("/ready")
def ready():
    return "OK", 200