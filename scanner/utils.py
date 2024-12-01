from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    """
    Decode a QR code from an image file.

    Args:
        image_path (str): Path to the image file containing the QR code

    Returns:
        str: Decoded text from the QR code if found, 'No Qr Code Detected' if no QR code is found

    Raises:
        Exception: If there is an error opening or processing the image
    """
    try:
        img = Image.open(image_path)
        decoded_objects = decode(img)
        if decoded_objects:
            # Get the first results
            return decoded_objects[0].data.decode('utf-8')
        return 'No Qr Code Detected'

    except Exception as e:
        print(f'Error While decoding {str(e)}')