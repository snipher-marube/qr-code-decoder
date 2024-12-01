# scanner/views.py
from django.shortcuts import render
from .forms import QRCodeForm
from .models import QRCode
from .utils import decode_qr_code
import os

def upload_qr_code(request):
    """
    View function to handle QR code image upload and decoding.

    GET: Displays an empty form for uploading QR code images
    POST: Processes the uploaded image, decodes the QR code, and displays results

    Args:
        request: HttpRequest object

    Returns:
        HttpResponse with either:
        - Upload form template for GET requests
        - Results template showing decoded content for successful POST requests
    """
    if request.method == "POST":
        form = QRCodeForm(request.POST, request.FILES)
        if form.is_valid():
            qr_code = form.save(commit=False)
            qr_code.image = form.cleaned_data['image']
            qr_code.save()

            # Verify the file path
            file_path = qr_code.image.path
            print(f"File path: {file_path}")
            if not os.path.exists(file_path):
                print("Error: File does not exist at the specified path.")

            # Decode the QR code
            qr_code.content = decode_qr_code(file_path)
            qr_code.save()

            return render(request, 'scanner/result.html', {'qr_code': qr_code})
    else:
        form = QRCodeForm()
    return render(request, 'scanner/upload.html', {'form': form})
