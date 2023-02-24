FROM python:3.9-alpine
RUN pip install flask filelock
COPY app.py /
CMD FLASK_APP=/app.py flask run --host=0.0.0.0