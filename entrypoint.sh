#!/bin/sh -l

cd "$GITHUB_WORKSPACE"

/find_depend_pkgs.py "$@"
