FROM python:3.9-alpine
RUN pip install flask
COPY server.py /
CMD FLASK_APP=/server.py flask run --host=0.0.0.0