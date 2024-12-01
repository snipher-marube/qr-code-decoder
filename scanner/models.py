from django.db import models

class QRCode(models.Model):
    """
    Model to store QR code images and their decoded content.

    Fields:
        image (ImageField): The uploaded QR code image file, stored in 'qrcode/' directory
        content (TextField): The decoded text content from the QR code, can be blank/null
        date_uploaded (DateTimeField): Timestamp of when the QR code was uploaded

    Methods:
        __str__: Returns the decoded content if available, otherwise "No Content"
    """
    image = models.ImageField(upload_to='qrcode/')
    content = models.TextField(blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content if self.content else "No Content"
