FROM python:3.7

RUN apt-get update
RUN apt-get -y install curl git

COPY Pipfile* /
RUN mkdir src
COPY src/* src/
COPY report.sh /usr/local/bin/rp_reviewdog

RUN cat /usr/local/bin/rp_reviewdog
RUN hash | grep rp_reviewdog
RUN which rp_reviewdog
RUN hash -r
RUN chmod a+x rp_reviewdog

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s
ENV PATH $PATH:./bin/
RUN echo "test circle ci"
