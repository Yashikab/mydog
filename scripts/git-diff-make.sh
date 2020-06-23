#!/bin/bash

# エラー即時終了
set -eu

if [ $# -ne 1 ]; then
    echo "Please specify the argument of make." 1>&2
    exit 1
fi

TARGETS=(python)
for TARGET in $TARGETS
do
    HAS_DIFF=`git diff --diff-filter=ACMR --name-only HEAD\^ HEAD --relative=$TARGET | head -1`
    if [ ! -z $HAS_DIFF ]; then
        ( cd ${TARGET} && make $1 )
    fi
done
