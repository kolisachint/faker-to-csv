#!/usr/bin/env bash

if [ -e "/app/main.py" ]; then
    python3 /app/main.py
fi

tail -f /dev/null

