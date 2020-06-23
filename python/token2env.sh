#!bin/sh
python /src/python/get_token.py
export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
rm /src/token.conf
