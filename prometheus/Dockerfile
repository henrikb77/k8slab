FROM python:3.9-alpine
RUN pip install prometheus_client
COPY pytest.py /
CMD python -u /pytest.py