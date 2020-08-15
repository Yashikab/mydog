FROM python:3.7

SHELL ["/bin/bash", "-c"]
RUN apt-get update
RUN apt-get -y install curl git

COPY Pipfile* /
RUN mkdir src
COPY src/* src/
COPY report.sh /usr/local/bin/rp_reviewdog
RUN chmod a+x /usr/local/bin/rp_reviewdog
RUN rp_reviewdog --test

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
RUN echo "test circle ci"
