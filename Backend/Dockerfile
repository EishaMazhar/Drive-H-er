FROM python:3.9-alpine3.14
WORKDIR /app
COPY requirements.txt
RUN pip install -r requirements.txt
COPY app ./app
EXPOSE 50000
CMD uvicorn app.main:app --host 0.0.0.0 --port 50000