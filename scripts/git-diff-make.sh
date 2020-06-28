#!/bin/bash

# エラー即時終了
set -eu

if [ $# -ne 1 ]; then
    echo "Please specify the argument of make." 1>&2
    exit 1
fi

TARGETS=(`find types -maxdepth 1 -mindepth 1 -type d`)
for TARGET in $TARGETS
do
    HAS_DIFF=`git diff --diff-filter=ACMR --name-only HEAD\^ HEAD --relative=$TARGET | head -1`
    if [ ! -z $HAS_DIFF ]; then
        echo "Pushing on" ${TARGET} "to docker"
        ( cd ${TARGET} && make $1 )
    else
        echo "No changes has founded"
    fi
done
