import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def sanitize_filename(filename):
    return "".join(c for c in filename if c.isalnum() or c in (' ', '.', '_')).rstrip()

def download_image_from_vsco(url, output_folder='images'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Connection': 'keep-alive',
    }
    
    # Make the request to the URL
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the image URL
    image = soup.find('img')
    if not image:
        print("Could not find the image on the page.")
        return

    image_url = image['src']
    
    # Ensure the URL is complete
    if not image_url.startswith(('http://', 'https://')):
        image_url = urljoin(url, image_url)
    
    # Get the image content
    image_response = requests.get(image_url, headers=headers)
    
    # Check if the request was successful
    if image_response.status_code != 200:
        print(f"Failed to retrieve the image. Status code: {image_response.status_code}")
        return
    
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Extract the filename and sanitize it
    parsed_url = urlparse(image_url)
    image_name = os.path.join(output_folder, sanitize_filename(os.path.basename(parsed_url.path)))
    
    # Save the image
    with open(image_name, 'wb') as f:
        f.write(image_response.content)
    
    print(f"Image successfully downloaded to {image_name}")

def download_images_from_file(file_path, output_folder='images'):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    
    for url in urls:
        url = url.strip()
        if url:
            download_image_from_vsco(url, output_folder)

# Example usage
file_path = "vsco_urls.txt"
download_images_from_file(file_path)