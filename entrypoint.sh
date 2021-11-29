#!/usr/bin/env bash

if [ -e "/app/main.py" ]; then
    python3 /app/main.py >> app.log 1>> app.log 2>> app.log
fi

tail -f /dev/null

