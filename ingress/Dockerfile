FROM python:3.9-alpine
RUN pip install flask
COPY app.py /
ENV VERSION=8.0
CMD FLASK_APP=/app.py flask run --host=0.0.0.0