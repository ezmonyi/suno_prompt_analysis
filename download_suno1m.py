import json
import os
import requests
from urllib.parse import urlparse

# Path to your JSONL file
jsonl_file = "metadata_uuid.jsonl"

# Folder to save downloaded audio
output_folder = "suno1m"
os.makedirs(output_folder, exist_ok=True)

# Function to download a file from a URL
def download_audio(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Iterate through JSONL
with open(jsonl_file, "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        audio_url = data.get("audio_url")
        if audio_url:
            # Get basename from URL
            parsed_url = urlparse(audio_url)
            filename = os.path.basename(parsed_url.path)
            save_path = os.path.join(output_folder, filename)
            download_audio(audio_url, save_path)
