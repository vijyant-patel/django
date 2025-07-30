from django import forms
from .models import ZipFileUpload

class ZipUploadForm(forms.ModelForm):
    class Meta:
        model = ZipFileUpload
        fields = ['file']
