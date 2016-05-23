# coding: utf-8

from os import path

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from documents.models import File


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['document', 'file']

    def clean_file(self):
        _uploaded_file_name = self.cleaned_data['file'].name
        _ext = path.splitext(_uploaded_file_name)[1]

        if (_ext):
            if not (_ext in settings.FILE_ALLOWED_EXT):
                raise ValidationError(
                    '''L'extension de fichier {} n'est pas autorisée \
                    (sont autorisés : {})'''.format(_ext, ', '.join(settings.FILE_ALLOWED_EXT)))
        else:
            raise ValidationError('Les noms de fichier sans extensions ne sont pas autorisés')
        return self.cleaned_data['file']
