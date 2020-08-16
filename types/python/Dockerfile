FROM python:3.7

SHELL ["/bin/bash", "-c"]
RUN apt-get update
RUN apt-get -y install curl git

COPY Pipfile* /
RUN mkdir src
COPY src/* src/
RUN mkdir /usr/local/bin/myscript
ENV PATH $PATH:/usr/local/bin/myscript
COPY script/* /usr/local/bin/myscript/
RUN chmod a+x /usr/local/bin/myscript/*
RUN rp_reviewdog --test

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
RUN echo "test circle ci"
