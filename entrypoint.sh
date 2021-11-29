#!/usr/bin/env bash

if [ -e "/app/main.py" ]; then
    python3 /app/main.py >> output.txt 1>> output.txt 2>> output.txt
fi

tail -f /dev/null

