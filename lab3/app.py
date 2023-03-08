import os
import threading
from flask import Flask


app = Flask(__name__)
lock = threading.Lock()

@app.route('/')
def root():
    lock.acquire()
    # do stuff
    lock.release()
    return f"App v3 running\n"

@app.route("/ready")
def ready():
    lock.acquire()
    # do stuff
    lock.release()
    return "OK", 200

@app.route("/live")
def live():
    lock.acquire()
    # do stuff
    lock.release()
    return "OK", 200

@app.route("/crash")
def crash():
    os._exit(1)
    return "Not gonna happen", 200

@app.route("/hang")
def hang():
    lock.acquire()
    return "Forgot to release lock\n", 200