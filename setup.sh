#!/bin/bash
# Setup script for Flet FilePicker Test App
# This script sets up the virtual environment and installs dependencies

# Change to the script's directory
cd "$(dirname "$0")"

echo "Setting up Flet FilePicker Test App..."
echo ""

# Check if Python 3 is available
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed or not in PATH"
    exit 1
fi

echo "Python version: $(python3 --version)"
echo ""

# Create virtual environment if it doesn't exist
if [ -d ".venv" ]; then
    echo "Virtual environment already exists."
    read -p "Do you want to recreate it? (y/N) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing virtual environment..."
        rm -rf .venv
    else
        echo "Using existing virtual environment."
        echo "To reinstall dependencies, run: .venv/bin/pip install -r requirements.txt"
        exit 0
    fi
fi

echo "Creating virtual environment..."
python3 -m venv .venv

if [ $? -ne 0 ]; then
    echo "Error: Failed to create virtual environment"
    exit 1
fi

echo "Installing dependencies..."
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "Setup complete!"
    echo ""
    echo "To run the app:"
    echo "  ./run.sh"
    echo ""
    echo "To build for macOS:"
    echo "  ./build-macos.sh"
else
    echo ""
    echo "Error: Failed to install dependencies"
    exit 1
fi
