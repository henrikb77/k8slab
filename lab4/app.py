from flask import Flask
from flask import request
import logging

log = logging.getLogger('werkzeug')
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello\n"

@app.route('/fib')
def fibonacci():
    nterms = int(request.args.get('nterms'))
    count = 0
    n1, n2 = 0, 1
    ret = ""
    while count < nterms:
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
       ret += f"{n1} "
    return f"{ret}\n"

@app.route("/ready")
def ready():
    return "OK", 200