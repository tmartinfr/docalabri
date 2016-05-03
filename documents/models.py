from __future__ import unicode_literals

from datetime import datetime, timedelta
from os import path
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Document(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expiration_date = models.DateField('expiration date', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    modification_date = models.DateTimeField('creation date', auto_now=True)
    #TODO: tags

    def __str__(self):
        return self.name

    # Returns True if document expires in less than one month.
    def expire_soon(self):
        if self.expiration_date < datetime.now().date() + timedelta(30):
            return True
        return False

# Do not change this function name, it could impact migrations.
def user_directory_path(instance, filename):
    uuid = uuid4()
    ext = path.splitext(filename)[1]
    return 'documents/user_{0}/{1}.{2}'.format(instance.document.user.id, uuid, ext)

@python_2_unicode_compatible
class File(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)

    def __str__(self):
        return self.file.name
