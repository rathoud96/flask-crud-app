FROM ubuntu:16.04
# MAINTANER Your Name "rathoreviveksingh960@gmail.com"

# We copy just the requirements.txt first to leverage Docker cache
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_CONFIG=development
ENV FLASK_APP=run.py

RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x docker-entrypoint.sh

EXPOSE 80

ENTRYPOINT [ "./docker-entrypoint.sh" ]

