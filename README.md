# Ubuntu_Requests

## Ubuntu Image Fetcher

This tool allows you to download images from the web in a safe and community-minded way.

### How to Use

1. Run the script:
	```bash
    windows
    python ubuntu_image_fetcher.py

    linux
	python3 ubuntu_image_fetcher.py
	```
2. Enter one or more image URLs, separated by commas, when prompted.
3. The images will be saved in the `Fetched_Images` folder.

**Features:**
- Handles multiple URLs at once
- Checks for duplicate images
- Warns about untrusted sources
- Only saves valid image files

**Requirements:**
- Python 3
- `requests` library (install with `pip install requests`)
