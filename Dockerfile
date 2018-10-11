FROM ubuntu:16.04

LABEL maintainer="phan.huy.hoang@framgia.com"

WORKDIR /code

COPY requirement_docker.txt .

RUN set -ex; \
	apt-get -y update; \
	apt-get install -y --no-install-recommends g++

RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype

RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils

RUN apt-get install -y python3-pip

RUN pip3 install --upgrade pip

RUN apt-get install -y --fix-missing \
	build-essential \
	cmake \
	gfortran \
	git \
	wget \
	curl \
	graphicsmagick \
	libgraphicsmagick1-dev \
	libatlas-dev \
	libavcodec-dev \
	libavformat-dev \
	libgtk2.0-dev \
	libjpeg-dev \
	liblapack-dev \
	libswscale-dev \
	pkg-config \
	python3-dev \
	python3-numpy \
	python3-setuptools \
	software-properties-common \
	zip \
	gir1.2-gstreamer-1.0 \
	gir1.2-gst-plugins-base-1.0 \
	python-gi python3-gi \
	libgstreamer1.0-dev \
	gstreamer1.0-plugins-good \
	ffmpeg \
	ubuntu-restricted-extras \
	&& apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN cd ~ && \
	mkdir -p dlib && \
	git clone -b 'v19.9' --single-branch https://github.com/davisking/dlib.git dlib/ && \
	cd  dlib/ && \
	python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA && \
	pip3 install dlib

RUN pip3 install --no-cache-dir -r requirement_docker.txt

COPY . .

EXPOSE 80

CMD python3 manage.py runserver 0.0.0.0:80