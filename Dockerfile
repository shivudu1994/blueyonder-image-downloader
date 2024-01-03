# Use the official Python image from Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the necessary directories and files to the container
COPY app.py .
COPY downloader downloader
COPY resources resources
COPY templates templates
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Command to run the application
CMD ["python", "app.py"]
