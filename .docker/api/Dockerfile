FROM ubuntu:16.04

MAINTAINER HDT <hoang.dinh.thoi@framgia.com>

RUN mkdir /code
RUN apt-get update
RUN apt-get install build-essential cmake
RUN apt-get install libopenblas-dev liblapack-dev
RUN apt-get install libx11-dev libgtk-3-dev
RUN apt-get install python python-dev python-pip
RUN apt-get install python3 python3-dev python3-pip
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 80

CMD python3 manage.py runserver 0.0.0.0:80
