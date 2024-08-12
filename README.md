# Pixel Manipulation for Image Encryption

## Description
The Pixel Manipulation for Image Encryption is a Python-based web application that allows users to encrypt and decrypt images. The application uses simple pixel manipulation techniques, such as shuffling and channel swapping, to secure images. Users provide an image file and a seed value, which is used for encryption and decryption processes.

## Features

- **Image Encryption and Decryption:** Encrypt and decrypt images using a seed value. The encryption process involves shuffling pixels and swapping color channels, while the decryption process reverses these operations.

- **Web Interface:** An intuitive web application interface allows users to upload image files and select whether to encrypt or decrypt them.

- **File Handling:** Supports uploading image files and returns the processed image as a downloadable file.

## Requirements

- Python 3.x
- Flask
- Pillow

### Install Dependencies
Install the required Python packages by running:
```bash
$ pip install flask
$ pip install pillow
