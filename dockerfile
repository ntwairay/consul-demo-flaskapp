FROM python:3.7-slim

ENV PORT=5000

COPY requirements.txt /app/requirements.txt

RUN pip3.7 install -r /app/requirements.txt

COPY src/ /app/src/

EXPOSE 5000

WORKDIR /app/src

CMD gunicorn -b 0.0.0.0:$PORT -w 4 wsgi:app
