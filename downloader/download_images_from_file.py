import os
import requests
import validators


def download_images_from_file(file_path, output_dir):
    """
    Downloads images from a list of URLs provided in a text file.

    Args:
    - file_path (str): Path to the file containing URLs.
    - output_dir (str): Directory where downloaded images will be saved.

    Returns:
    - str: Result message indicating the success or failure of the download process.
    """
    try:
        with open(file_path, 'r') as file:
            urls = file.readlines()

            if not any(urls):
                return "No URLs found in the file."

            for url in urls:
                url = url.strip()
                if url and validators.url(url):
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            image_name = url.split('/')[-1]
                            image_path = os.path.join(output_dir, image_name)
                            with open(image_path, 'wb') as img_file:
                                img_file.write(response.content)
                            print(f"Downloaded: {image_name}")
                        else:
                            print(f"Failed to download: {url} - Status code: {response.status_code}")
                    except requests.RequestException as e:
                        print(f"Failed to download: {url} - {e}")
                else:
                    print(f"Invalid URL: {url}")

            downloaded_images = len(
                [name for name in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, name))])
            if downloaded_images > 0:
                return "Download complete."
            else:
                return "Failed to download any images."
    except FileNotFoundError:
        return "File not found."
    except Exception as ex:
        return f"An error occurred: {ex}"
