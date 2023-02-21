from flask import Flask
from flask import request
import logging

log = logging.getLogger('werkzeug')
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello\n"

@app.route('/div')
def divide_by_three():
    dividend = int(request.args.get('dividend')) 
    return str(dividend/3) + "\n"