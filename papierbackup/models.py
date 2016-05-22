# coding: utf8

from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True, error_messages={'unique': 'Cette adresse e-mail est déjà enregistrée'})
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
