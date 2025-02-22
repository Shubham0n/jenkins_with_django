#!/bin/bash

set -e  # Exit script on error

echo "Detected OS: $OSTYPE"

# Set Python and virtual environment activation paths
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    PYTHON_EXEC="py"
    VENV_PATH="env/Scripts/activate"
    VENV_CREATE_CMD="py -m venv env"
else
    PYTHON_EXEC="python3"
    VENV_PATH="env/bin/activate"
    VENV_CREATE_CMD="python3 -m venv env"
fi

# Create virtual environment if not exists
if [[ ! -d "env" ]]; then
    echo "Virtual environment not found. Creating one..."
    $VENV_CREATE_CMD || { echo "Failed to create virtual environment"; exit 1; }
else
    echo "Virtual environment found. Activating..."
fi

# Activate the virtual environment
source $VENV_PATH

# Check if the virtual environment is activated
if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Failed to activate virtual environment."
    exit 1
fi

echo "Virtual environment activated successfully!"

# Upgrade pip and install dependencies
if [[ -f "requirements.txt" ]]; then
    echo "Installing dependencies..."
    $PYTHON_EXEC -m pip install --upgrade pip
    $PYTHON_EXEC -m pip install -r requirements.txt
else
    echo "requirements.txt not found. Skipping installation."
fi

# Run Django commands
echo "Running Django migrations and server..."
$PYTHON_EXEC manage.py makemigrations || { echo "makemigrations failed"; exit 1; }
$PYTHON_EXEC manage.py migrate || { echo "migrate failed"; exit 1; }
$PYTHON_EXEC manage.py collectstatic --noinput || { echo "collectstatic failed"; exit 1; }
$PYTHON_EXEC manage.py add_user --email "dev_classdekho@gmail.com" --password "admin" --is_superuser "true" --is_staff "true" --is_active "true"
# $PYTHON_EXEC manage.py runserver