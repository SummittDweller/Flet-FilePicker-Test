#!/bin/bash
# Run script for Flet FilePicker Test App
# This script activates the virtual environment and runs the Flet application

# Change to the script's directory
cd "$(dirname "$0")"

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run: ./setup.sh"
    exit 1
fi

# Activate virtual environment and run the app
echo "Starting Flet FilePicker Test App..."
.venv/bin/python main.py
