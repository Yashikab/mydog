FROM docker:dind

RUN apk add bash
SHELL ["/bin/bash", "-c"]
# RUN apt-get update
RUN apk --update --no-cache add --virtual curl git jq

# # pythonのinstall
RUN wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
# RUN apk add zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel
RUN apk --update --no-cache add --virtual build-temp build-base openssl make automake gcc g++ subversion
RUN tar zxvf Python-3.7.9.tgz
WORKDIR /Python-3.7.9
RUN ls -l
RUN ./configure
RUN make
RUN make install
RUN ln -s /usr/local/python/bin/python3 /usr/local/bin/python
RUN ln -s /usr/local/python/bin/pip3.7 /usr/local/bin/pip
RUN python --version
RUN pip --version
# RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
# RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s

# COPY Pipfile* /
# RUN mkdir src
# COPY src/ src/
# ENV PYTHONPATH $PYTHONPATH:/src/module
# RUN mkdir /usr/local/bin/myscript
# ENV PATH $PATH:/usr/local/bin/myscript
# COPY script/* /usr/local/bin/myscript/
# RUN chmod a+x /usr/local/bin/myscript/*

# RUN pip install pipenv==2018.11.26
# RUN pipenv install --dev --system
# RUN pip install -e src/
# ENV PATH $PATH:./bin/
# RUN rp_reviewdog --help
