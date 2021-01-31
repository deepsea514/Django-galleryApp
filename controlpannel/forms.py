from django import forms
from .models import Product


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Product
        fields = ('P_image',)