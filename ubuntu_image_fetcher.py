import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web")
    print()
    print("Please enter image URLs (comma-separated):")
    url_input = input().strip()
    urls = [u.strip() for u in url_input.split(',') if u.strip()]
    if not urls:
        print("No URLs provided. Exiting.")
        return

    os.makedirs("Fetched_Images", exist_ok=True)
    existing_files = set(os.listdir("Fetched_Images"))

    for url in urls:
        print(f"\nProcessing: {url}")
        try:
            # Basic precaution: warn if not HTTPS
            if not url.lower().startswith("https://"):
                print("  [!] Warning: URL is not HTTPS. Downloading from untrusted sources can be risky.")

            response = requests.get(url, timeout=10, stream=True)
            response.raise_for_status()

            # Check important headers
            content_type = response.headers.get('Content-Type', '')
            if not content_type.startswith('image/'):
                print(f"  ✗ Skipped: Content-Type '{content_type}' is not an image.")
                continue
            content_length = response.headers.get('Content-Length')
            if content_length and int(content_length) > 10*1024*1024:
                print("  ✗ Skipped: Image is larger than 10MB.")
                continue

            # Extract filename
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            if not filename:
                filename = "downloaded_image.jpg"

            # Prevent duplicate downloads
            filepath = os.path.join("Fetched_Images", filename)
            if filename in existing_files:
                print(f"  ✗ Skipped: '{filename}' already exists.")
                continue

            # Save the image
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            existing_files.add(filename)

            print(f"  ✓ Successfully fetched: {filename}")
            print(f"  ✓ Image saved to {filepath}")
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Connection error: {e}")
        except Exception as e:
            print(f"  ✗ An error occurred: {e}")
    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()