FROM python:3.7

RUN apt-get update
RUN apt-get -y install curl git

COPY Pipfile* /
RUN mkdir src
COPY src/* src/

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
