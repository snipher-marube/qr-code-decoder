# scanner/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_qr_code, name='upload_qr_code'),
]
