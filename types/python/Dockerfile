FROM python:3.7

RUN apt-get update
RUN apt-get -y install curl git

COPY Pipfile* /
RUN mkdir src
COPY src/* src/
COPY report.sh /

ARG APP_ID
ENV APP_ID ${APP_ID}
ARG INSTALLATION_ID
ENV INSTALLATION_ID ${INSTALLATION_ID}
ARG PRIVATE_KEY
ENV PRIVATE_KEY ${PRIVATE_KEY}

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
RUN echo "test circle ci"
