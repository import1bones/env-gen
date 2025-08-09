#!/bin/sh
# scripts/bootstrap.sh - Bootstrap script for macOS/Linux

# Check if python3 is installed
if ! command -v python3 >/dev/null 2>&1; then
    echo "Python3 is not installed. Attempting to install..."
    # Try to install python3 using common package managers
    if command -v brew >/dev/null 2>&1; then
        brew install python3
    elif command -v apt-get >/dev/null 2>&1; then
        sudo apt-get update && sudo apt-get install -y python3
    elif command -v yum >/dev/null 2>&1; then
        sudo yum install -y python3
    else
        echo "Please install Python3 manually."
        exit 1
    fi
fi

# Run the main Python CLI
exec python3 -m envgen.cli "$@"
