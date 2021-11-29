#!/usr/bin/env bash

if [ -e "requirements.txt" ]; then
    pip3 --disable-pip-version-check --no-cache-dir \
      install -r requirements.txt
fi

if [ -e "main.py" ]; then
    python3 main.py
fi

tail -f /dev/null

