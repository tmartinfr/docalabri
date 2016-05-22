from django import forms
from django.forms import ModelForm

from documents.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['document', 'file']
