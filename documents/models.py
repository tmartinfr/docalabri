from __future__ import unicode_literals

import mimetypes

import os
from datetime import datetime, timedelta
from uuid import uuid4

from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Document(models.Model):
    name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category)
    expiration_date = models.DateField('expiration date', null=True, blank=True)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    modification_date = models.DateTimeField('creation date', auto_now=True)

    def __str__(self):
        if self.name:
            return "{} - {}".format(self.category.name, self.name)
        return self.category.name

    # Returns True if document expires in less than one month.
    def expire_soon(self):
        if self.expiration_date < datetime.now().date() + timedelta(30):
            return True
        return False

    class Meta:
        ordering = ['-modification_date', '-creation_date']


# Do not change this function name, it could impact migrations.
def user_directory_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    return 'documents/user_{}/{}/{}{}'.format(
        instance.document.user.id,
        instance.document.id,
        uuid4(),
        ext
    )


@python_2_unicode_compatible
class File(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path)
    creation_date = models.DateTimeField('creation date', auto_now_add=True)
    # According to RFC6838, MIME-types are 255 caracters max.
    # http://tools.ietf.org/html/rfc6838#section-4.2

    class Meta:
        ordering = ['creation_date']

    def __str__(self):
        return self.file.name

    def slugname(self):
        # TODO(swann): display unique file id per document instead of uuid.
        basename = self.file.url.split('/')[-1]
        document_slug = slugify(self.document)
        return "{}-{}".format(document_slug, basename)

    def mimetype(self):
        return mimetypes.guess_type(self.file.url)[0]
