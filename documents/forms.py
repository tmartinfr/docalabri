# coding: utf-8

from os import path
import mimetypes

from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError

import logging
import magic

from .models import File


logger = logging.getLogger(__name__)


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['document', 'file']

    def clean_file(self):
        _uploaded_file_name = self.cleaned_data['file'].name
        _ext = path.splitext(_uploaded_file_name)[1]
        try:
            _mimetype = magic.from_buffer(self.cleaned_data['file'].file.read(1024), mime=True)
        except magic.MagicException as e:
            logger.error(e)
            raise ValidationError(
                'Une erreur est survenue lors du traitement du fichier téléversé!'
            )

        _expected_mimetype = mimetypes.guess_type(_uploaded_file_name)[0]
        if (_ext):
            if _ext.lower() not in settings.FILE_ALLOWED_EXT:
                raise ValidationError(
                    '''L'extension de fichier {} n'est pas autorisée \
                    (sont autorisés : {})'''.format(_ext, ', '.join(settings.FILE_ALLOWED_EXT)))
            if _mimetype != _expected_mimetype:
                raise ValidationError('{} ne semble pas être un fichier {} valide'.format(_uploaded_file_name, _ext))

        else:
            raise ValidationError('Les noms de fichier sans extensions ne sont pas autorisés')
        return self.cleaned_data['file']
