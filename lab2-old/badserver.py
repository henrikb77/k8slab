from flask import Flask
from flask_apscheduler import APScheduler
import logging

log = logging.getLogger('werkzeug')
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello\n"

def test_job():
    log.info('I am working...')

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
scheduler.add_job(id='test-job', func=test_job, trigger='interval', seconds=1)