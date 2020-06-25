#!bin/sh
if [ $# -ne 1 ]; then
    echo "input target directory" 1>&2
    exit 1

else
    python /src/get_token.py
    export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
    rm /src/token.conf

    flake8 $1 | reviewdog -efm="%f:%l:%c: %m" -reporter=github-pr-review
fi
