#!/bin/bash
# Build script for macOS with entitlements for FilePicker
# This script builds a macOS .app bundle with the necessary entitlements
# to allow FilePicker to work properly on macOS

# Change to the script's directory
cd "$(dirname "$0")"

# Check if .venv exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found!"
    echo "Please run: ./setup.sh"
    exit 1
fi

echo "Building macOS app with FilePicker entitlements..."
echo "This may take several minutes..."

# Build the macOS app with the required entitlement for file access
.venv/bin/flet build macos \
    --macos-entitlements com.apple.security.files.user-selected.read-write=true

# Check if build was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "Build successful!"
    echo "Opening the app..."
    echo ""
    
    # Find and open the built app
    APP_PATH=$(find dist/macos -name "*.app" -type d | head -n 1)
    if [ -n "$APP_PATH" ]; then
        echo "App location: $APP_PATH"
        open "$APP_PATH"
    else
        echo "Warning: Could not find the built .app file in dist/macos/"
    fi
else
    echo ""
    echo "Build failed! Please check the error messages above."
    exit 1
fi
