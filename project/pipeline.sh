#!/bin/bash
# Change to the project root directory
cd "$(dirname "$0")/.."
# Activate the virtual environment
source venv/Scripts/activate
# Run the data processing script
"$(dirname "$0")/../venv/Scripts/python.exe" project/data_processing.py