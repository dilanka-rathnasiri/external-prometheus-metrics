FROM python:alpine

WORKDIR /app

COPY src /app/src
COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ENV SERVER_PORT=8000

EXPOSE 8000

CMD [ "python", "/app/src/main.py" ]
