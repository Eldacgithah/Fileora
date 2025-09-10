
# Fileora

Fileora is a simple CLI tool to upload files and images to Catbox.moe, providing permanent direct links without registration or API keys. Works on Windows, macOS, and Linux.

## Features

- Upload any file or image quickly
- Get a permanent direct link instantly
- Works without registration or API keys
- Install globally and use from any directory
- Automatically hides the project folder after installation

## Installation

### Linux/macOS

Run the installer in one command using curl:

curl -s https://raw.githubusercontent.com/Eldacgithah/Fileora/main/install_fileora.py | python3

Or using wget:

wget -qO- https://raw.githubusercontent.com/Eldacgithah/Fileora/main/install_fileora.py | python3

### Windows (PowerShell)

Invoke-WebRequest -Uri "https://raw.githubusercontent.com/Eldacgithah/Fileora/main/install_fileora.py" -OutFile "$env:TEMP\\install_fileora.py"; python "$env:TEMP\\install_fileora.py"

This will:
1. Clone the project into a temporary folder in the current directory
2. Install required dependencies
3. Install the CLI tool globally (`fileora` command)
4. Move the project folder to a hidden location

## Usage

fileora path/to/your/file.jpg

- Works with images, videos, and any file type supported by Catbox.moe
- You can provide either a relative or absolute file path

### Examples

Linux/macOS:
fileora example.png
fileora ~/Downloads/video.mp4

Windows (Command Prompt or PowerShell):
fileora C:\\Users\\User\\Pictures\\example.png
fileora D:\\Videos\\clip.mp4

## Requirements

- Python 3.6+
- Git installed and available in PATH
- Internet connection

## Contributing

Feel free to fork the repository and submit pull requests. Bug reports and feature suggestions are welcome.
