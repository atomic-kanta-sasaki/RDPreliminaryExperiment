FROM python:3.7.3
WORKDIR /var/www/html
EXPOSE 80
USER root
SHELL ["/bin/bash", "-c"]
ENV DEBCONF_NOWARNINGS yes
RUN apt-get update && apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

RUN apt-get update && apt-get install -y \
    xdotool \
    libgirepository1.0-dev
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt-get install -y vim less
RUN pip install rssi