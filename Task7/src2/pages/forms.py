from django import forms
from .models import Document, Image


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["name", "imagefile"]

