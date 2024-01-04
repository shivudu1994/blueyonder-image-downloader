# Blueyonder Image Downloader

This repository contains an image downloading application that allows users to download images from URLs provided in a text file.

## Usage

### Prerequisites
- Python 3.9 or higher

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/shivudu1994/blueyonder-image-downloader.git
    cd blueyonder-image-downloader
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
To run the image downloader, execute the following command:
```bash
python app.py
```

## Docker Usage

### Building the Docker Image

To build the Docker image, use the provided Dockerfile:

```bash
docker build -t image-downloader .
```
## Running the Docker Container

To run the Docker container with the built image:

```bash
docker run -p 5001:5001 image-downloader
```

## Accessing the Application

Once the Docker container is running, navigate to `http://localhost:5001` in your web browser.

1. Open your preferred web browser.
2. Enter `http://localhost:5001` in the address bar.
3. Use the interface to upload a text file containing URLs.
4. Ensure the text file contains valid URLs for images you want to download.

