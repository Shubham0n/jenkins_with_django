#!/bin/bash

set -e

# Detect OS and check if virtual environment exists
if [[ -d "env" ]]; then
    echo "Virtual environment found. Activating..."
else
    echo "Virtual environment not found. Creating one..."
    if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        py -m venv env
    elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
        python3 -m venv env
    else
        echo "Unsupported OS"
        exit 1
    fi
fi


# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source ./env/Scripts/activate  # Windows (Git Bash)
elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
    source ./env/bin/activate  # macOS/Linux
else
    echo "Unsupported OS"
    exit 1
fi


# Verify if the virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

echo "Virtual environment activated successfully!"


# Install dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping installation."
fi


# Git Bash on Windowss
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    py manage.py makemigrations
    py manage.py migrate
    py manage.py collectstatic --noinput
    py manage.py runserver

# macOS/Linux
elif [[ "$OSTYPE" == "darwin" || "$OSTYPE" == "linux-gnu" ]]; then
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py collectstatic --noinput
    python3 manage.py runserver
else
    echo "Unsupported OS"
    exit 1
fi
