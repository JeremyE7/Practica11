FROM python:3.8-slim-buster

RUN apt-get update && \
    apt-get install -y python3-dev default-libmysqlclient-dev build-essential && \
    apt-get clean

WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . /app

EXPOSE 8000

CMD ["flask", "run", "--host=0.0.0.0" ]

