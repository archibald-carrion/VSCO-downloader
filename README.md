# VSCO downloader
Python application that download image from vsco, it use beautifulsoup4 and requests library to download image from vsco.
This application was created for educational purposes only.
The original objective was to use it to create dataset for machine learning.

## Installation
```bash
pip install -r requirements.txt
```
*Note:* You need to have python installed on your computer to run this application.

The requirements.txt file contains the libraries that are needed to run this application, the requirements.txt file does not specify the version of the libraries, so it is possible that the application will not work if the libraries are updated.
The application was tested with the following versions of the libraries:
- beautifulsoup4==4.12.3
- requests==2.31.0

## Usage
```bash
python vsco_downloader.py
```
## Use guide
1. Enter the list of vsco url that you want to download in the `vsco_url.txt` file using the following format:
```txt
https://vsco.co/username/media/123image0
https://vsco.co/username/media/123image1
```
