from flask import Flask, render_template, request
from downloader.download_images_from_file import download_images_from_file
import os
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

# Set the UPLOAD_FOLDER configuration variable
app.config['UPLOAD_FOLDER'] = 'resources/uploads'  # Replace 'uploads' with your desired directory name

# Define the number of worker threads
NUM_WORKER_THREADS = 4

# Create a thread pool executor
executor = ThreadPoolExecutor(max_workers=NUM_WORKER_THREADS)


@app.route('/')
def index():
    """
    Renders the index.html template for the homepage.
    """
    return render_template('index.html')


def handle_download(file_path, output_directory):
    """
    Initiates the image download process.
    """
    try:
        result = download_images_from_file(file_path, output_directory)
        print(result)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


@app.route('/download', methods=['POST'])
def download():
    """
    Handles the file upload and initiates image download process using worker threads.

    Returns:
        str: Message after attempting to start the download process.
    """
    try:
        file = request.files['file']
        if file.filename.endswith('.txt'):
            # Create the upload folder if it doesn't exist
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            output_directory = 'resources/downloaded_images'  # Replace with your desired output directory

            # Submit the download task to the thread pool
            executor.submit(handle_download, file_path, output_directory)

            return "Download process completed."
        else:
            return "Please upload a text file."
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
