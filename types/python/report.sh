#!bin/sh
if [ $# -ne 1 ]; then
    echo "input target directory" 1>&2
    exit 1

else
    python /src/get_token.py
    export REVIEWDOG_GITHUB_API_TOKEN=`cat /src/token.conf`
    rm /src/token.conf

    echo $1
    cat flake8 $1 | reviewdog -efm="%f:%l:%c: %m" -reporter=github-pr-review > comment

    if [ ! -s comment ]; then
        echo ":100: All OK!" > comment
    fi

    curl -X POST \
        -H "Authorization: token ${REVIEWDOG_GITHUB_API_TOKEN}" \
        -H "Accept: application/json" \
        -H "Content-Type:application/json" \
        -d "{\"body\": \"$(cat comment)\"}" \
        "https://api.github.com/repos/${DRONE_REPO_OWNER}/${DRONE_REPO_NAME}/issues/${DRONE_PULL_REQUEST}/comments"

fi
