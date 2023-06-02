#!/bin/sh -l

cd "$GITHUB_WORKSPACE"

/find_depend_pkgs.py "$@" |tee /output.txt

echo "stdout=$(cat /output.txt)" >> $GITHUB_OUTPUT
