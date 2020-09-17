FROM python:3.7

SHELL ["/bin/bash", "-c"]

RUN apt-get update
RUN apt-get -y install curl git jq
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y

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
