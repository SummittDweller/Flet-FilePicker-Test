# Flet-FilePicker-Test

A test application demonstrating Flet's FilePicker functionality on macOS, built with the latest version of Flet and proper macOS entitlements.

## Overview

This project provides a simple GUI application that tests various file picker operations:
- Pick a single file
- Pick multiple files
- Pick a directory
- Save file dialog

The app is built with [Flet](https://flet.dev/) 0.80.0 and includes the necessary macOS entitlements to allow FilePicker operations to work properly.

## Requirements

- Python 3.8 or later
- macOS (for building the .app bundle)
- VSCode (recommended for development)

## Quick Start

### 1. Setup Virtual Environment

For initial setup or if the virtual environment is missing, run:

```bash
./setup.sh
```

This will create the virtual environment and install all dependencies. If you prefer to do it manually:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 2. Run the Application (Development Mode)

From the project directory or VSCode terminal:

```bash
./run.sh
```

This will launch the Flet application in development mode with hot reload enabled.

### 3. Build macOS Application

To build a standalone macOS .app bundle with the necessary entitlements:

```bash
./build-macos.sh
```

This script:
- Builds the macOS application bundle
- Applies the `com.apple.security.files.user-selected.read-write=true` entitlement
- Automatically opens the built application

The built app will be located in `dist/macos/`.

### Alternative Build Command

You can also use the flet alias approach mentioned in the requirements:

```bash
alias flet-test='.venv/bin/flet build macos --macos-entitlements com.apple.security.files.user-selected.read-write=true && open dist/macos/*.app'
flet-test
```

## Project Structure

```
Flet-FilePicker-Test/
├── .venv/              # Virtual environment (not in git)
├── main.py             # Main Flet application
├── setup.sh            # Initial setup script
├── run.sh              # Development run script
├── build-macos.sh      # macOS build script with entitlements
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Features

The test application provides buttons to test different FilePicker scenarios:

1. **Pick Single File**: Opens a file picker allowing selection of one file (filtered by extensions: txt, pdf, png, jpg, jpeg)
2. **Pick Multiple Files**: Opens a file picker allowing selection of multiple files
3. **Pick Directory**: Opens a directory picker
4. **Save File**: Opens a save file dialog with suggested filename and extensions

Each operation displays the selected file path(s) or directory in the result area.

## macOS Entitlements

To allow FilePicker to work properly on macOS, the app requires the following entitlement:

```
com.apple.security.files.user-selected.read-write=true
```

This entitlement is automatically applied when using the `build-macos.sh` script or the build command with `--macos-entitlements` flag.

## Development in VSCode

1. Open the project folder in VSCode
2. Open the integrated terminal (`` Ctrl+` `` or `` Cmd+` ``)
3. Run `./run.sh` to start the application
4. Make changes to `main.py` - Flet's hot reload will automatically update the app

## Troubleshooting

### Virtual Environment Not Found

If you see an error about missing .venv:
```bash
python3 -m venv .venv
.venv/bin/pip install flet
```

### Build Fails

Make sure you have the latest Flet CLI:
```bash
.venv/bin/pip install --upgrade flet
```

### FilePicker Not Working on macOS

Ensure you're running the built .app bundle (not the Python script directly) with the proper entitlements applied via `build-macos.sh`.

## License

This is a test application for demonstration purposes.
