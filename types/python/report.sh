#!/bin/sh
if [ $# -ne 1 ]; then
    echo "input target directory" 1>&2
    exit 1
elif [ $1 = '--test' ]; then
    echo "command is available"
    exit 0
else
    python /src/get_token.py
    export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
    rm /src/token.conf

    echo $1
    flake8 $1 | reviewdog -reporter="github-pr-review" -f=pep8 > content

    if [ ! -s content ]; then
        echo ":100: All OK!" > comment
    else
        lines=$(cat content | wc -l)
        echo "you have ${lines} warnings or errors on python style codes." > comment
    fi

    curl -X POST \
        -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
        -H "Accept: application/json" \
        -H "Content-Type:application/json" \
        -d "{\"body\": \"$(cat comment)\"}" \
        "https://api.github.com/repos/${DRONE_REPO_OWNER}/${DRONE_REPO_NAME}/issues/${DRONE_PULL_REQUEST}/comments"
    rm comment
    rm content

fi
