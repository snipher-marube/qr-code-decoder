# QR Code Decoder

A Django web application that allows users to upload and decode QR code images.

## Features

- Upload QR code images through a web interface
- Decode QR codes using the pyzbar library
- Store QR code images and decoded content in a database
- Display decoded QR code content to users

## Installation

1. Clone the repository:
    ```bash 
        clone https://github.com/snipher-marube/qr-code-decoder.git```
2. Create and activate a virtual environment:
    ```bash 
    python3 -m venv venv```
    ```bash 
    source venv/bin/activate```
3. Install the required packages:
```bash pip install -r requirements.txt```
4. Run the Django server:
```bash python manage.py runserver```
5. Access the web application at http://127.0.0.1:8000/

## Usage

1. Upload a QR code image by clicking the "Choose File" button and selecting an image file.
2. Click the "Upload" button to decode the QR code.
3. View the decoded content below the upload form.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.






