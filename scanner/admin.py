from django.contrib import admin

from .models import QRCode

@admin.register(QRCode)
class QrCodeAdmin(admin.ModelAdmin):
    list_display = ['content', 'date_uploaded']
