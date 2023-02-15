FROM python:3.9-alpine
RUN pip install flask Flask-APScheduler
COPY badserver.py /
CMD FLASK_APP=/badserver.py flask run --host=0.0.0.0