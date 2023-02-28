FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask prometheus_client

EXPOSE 8001

CMD ["python", "app.py"]