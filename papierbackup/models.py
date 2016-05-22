from django.db import models


class Contact(models.Model):
    email = models.EmailField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
