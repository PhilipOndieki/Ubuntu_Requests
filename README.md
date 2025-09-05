# Ubuntu Image Fetcher

A Python tool for downloading images from URLs, inspired by Ubuntu philosophy: *"I am because we are"*

## Features

- Download single or multiple images
- Automatic duplicate detection
- Safe filename handling
- Content validation
- Collection statistics

## Installation

```bash
git clone https://github.com/yourusername/Ubuntu_Requests.git
cd Ubuntu_Requests
pip install requests
```

## Usage

```bash
python ubuntu_image_fetcher.py
```

Follow the interactive menu to:
1. Enter image URLs (single, multiple, or from file)
2. View your collection stats
3. Force download duplicates

## Example

```
Welcome to the Ubuntu Image Fetcher
Please enter the image URL: https://example.com/image.jpg
✓ Successfully fetched: image.jpg
✓ Image saved to Fetched_Images/image.jpg

Connection strengthened. Community enriched.
```

## Requirements

- Python 3.6+
- requests library

## File Structure

```
Ubuntu_Requests/
├── ubuntu_image_fetcher.py    # Main script
├── Fetched_Images/            # Downloaded images
└── README.md                  # This file
```

## Ubuntu Philosophy

This tool embodies Ubuntu principles:
- **Community**: Connects to the global web
- **Respect**: Handles errors gracefully
- **Sharing**: Organizes images for later use
- **Practicality**: Solves real needs safely
