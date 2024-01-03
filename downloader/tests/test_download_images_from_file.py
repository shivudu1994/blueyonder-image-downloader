import os
import unittest
from unittest.mock import patch
from downloader.download_images_from_file import download_images_from_file
import requests


class TestDownloadImagesFromFile(unittest.TestCase):
    """Test cases for the download_images_from_file function."""

    def setUp(self):
        """Create a test directory for downloaded files."""
        self.test_output_dir = 'test_downloads'
        os.makedirs(self.test_output_dir, exist_ok=True)

    def tearDown(self):
        """Remove the test directory and its contents."""
        if os.path.exists(self.test_output_dir):
            for file in os.listdir(self.test_output_dir):
                file_path = os.path.join(self.test_output_dir, file)
                os.remove(file_path)
            os.rmdir(self.test_output_dir)

    def test_download_images(self):
        """Test the download functionality with valid URLs."""
        test_urls_file = 'test_urls.txt'
        with open(test_urls_file, 'w') as file:
            file.write('https://example.com/image1.jpg\n')
            file.write('https://example.com/image2.jpg\n')

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.content = b'Fake image content'

            result = download_images_from_file(test_urls_file, self.test_output_dir)

            self.assertTrue(result.startswith('Download complete.'))
            self.assertEqual(len(os.listdir(self.test_output_dir)), 2)

    def test_invalid_file(self):
        """Test behavior when the specified file does not exist."""
        result = download_images_from_file('nonexistent.txt', self.test_output_dir)
        self.assertEqual(result, 'File not found.')

    def test_no_urls(self):
        """Test behavior when the file contains no URLs."""
        test_empty_file = 'empty_file.txt'
        with open(test_empty_file, 'w') as file:
            file.write('')

        result = download_images_from_file(test_empty_file, self.test_output_dir)
        self.assertEqual(result, 'No URLs found in the file.')

    def test_invalid_urls(self):
        """Test behavior when the file contains invalid URLs."""
        test_invalid_urls_file = 'invalid_urls.txt'
        with open(test_invalid_urls_file, 'w') as file:
            file.write('invalid_url\n')
            file.write('https://example.com/valid.jpg\n')

        with patch('requests.get', side_effect=requests.RequestException('Fake exception')):
            result = download_images_from_file(test_invalid_urls_file, self.test_output_dir)

        self.assertEqual(result, 'Failed to download any images.')
        self.assertEqual(len(os.listdir(self.test_output_dir)), 0)


if __name__ == '__main__':
    unittest.main()
