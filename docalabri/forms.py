
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from .models import Contact


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        # Add CSS class used by Bootstrap.
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].label = "Identifiant"
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].label = "Mot de passe"
        # Remove semicolon after fields name
        self.label_suffix = ''


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['email']
