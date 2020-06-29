FROM python:3.7

RUN apt-get update
RUN apt-get -y install curl git

COPY /python/Pipfile* /
RUN mkdir src
COPY /python/src/* src/
COPY /python/report.sh /

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
RUN echo "test circle ci"
