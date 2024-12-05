#!/bin/bash
# Change to the project root directory
cd "$(dirname "$0")/.."

# Activate the virtual environment
source venv/Scripts/activate

# Run the tests
python3 -m unittest discover -s project -p 'test_pipeline.py'