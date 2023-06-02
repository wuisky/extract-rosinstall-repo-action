FROM python:3-alpine

COPY find_depend_pkgs.py /find_depend_pkgs.py
COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]