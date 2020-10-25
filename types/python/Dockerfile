# imageをdocker:dindにし、python3.7を手動でインストール、コマンド設定でpython, pipコマンドで動くようにする
FROM python:3.7

SHELL ["/bin/bash", "-c"]
RUN apt-get update
RUN apt-get -y install curl git jq

# install mysql
RUN set -ex; \
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
	key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --batch --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	gpg --batch --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \
	gpgconf --kill all; \
	rm -rf "$GNUPGHOME"; \
	apt-key list > /dev/null
ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.32-1debian10

RUN echo "deb http://repo.mysql.com/apt/debian/ buster mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list
RUN apt-get update
RUN { \
		echo mysql-community-server mysql-community-server/data-dir select ''; \
		echo mysql-community-server mysql-community-server/root-pass password ''; \
		echo mysql-community-server mysql-community-server/re-root-pass password ''; \
		echo mysql-community-server mysql-community-server/remove-test-db select false; \
	} | debconf-set-selections \
	&& apt-get update && apt-get install -y mysql-server="${MYSQL_VERSION}"

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && apt-get update -y && apt-get install google-cloud-sdk -y
RUN curl -sfL https://raw.githubusercontent.com/reviewdog/reviewdog/master/install.sh | sh -s

COPY Pipfile* /
RUN mkdir src
COPY src/ src/
ENV PYTHONPATH $PYTHONPATH:/src/module
RUN mkdir /usr/local/bin/myscript
ENV PATH $PATH:/usr/local/bin/myscript
COPY script/* /usr/local/bin/myscript/
RUN chmod a+x /usr/local/bin/myscript/*

RUN pip install pipenv==2018.11.26
RUN pipenv install --dev --system
RUN pip install -e src/
ENV PATH $PATH:./bin/
RUN rp_reviewdog --help
RUN rp_pytest --help
RUN pr_comment --help
RUN mysql --version
