#!/bin/bash

# Python Virtual Environment Setup Script
# Creates and activates a virtual environment in the current directory

set -e  # Exit on any error

VENV_NAME="venv"

echo "Setting up Python virtual environment..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: python3 is not installed or not in PATH"
    exit 1
fi

# Check if virtual environment already exists
if [ -d "$VENV_NAME" ]; then
    echo "Virtual environment '$VENV_NAME' already exists."
    read -p "Do you want to remove it and create a new one? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "Removing existing virtual environment..."
        rm -rf "$VENV_NAME"
    else
        echo "Using existing virtual environment."
    fi
fi

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_NAME" ]; then
    echo "Creating virtual environment '$VENV_NAME'..."
    python3 -m venv "$VENV_NAME"
fi

# Activate virtual environment
echo "Activating virtual environment..."
source "$VENV_NAME/bin/activate"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

echo "Virtual environment setup complete!"
echo ""
echo "Virtual environment is now active."
echo "To activate it manually in the future, run:"
echo "    source $VENV_NAME/bin/activate"
echo ""
echo "To deactivate, run:"
echo "    deactivate"
echo ""
echo "Current Python path: $(which python)"
echo "Python version: $(python --version)"
