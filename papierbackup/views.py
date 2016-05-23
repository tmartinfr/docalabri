from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView

from .forms import CustomAuthenticationForm, ContactForm


class IndexView(TemplateView):
    template_name = "papierbackup/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['auth_form'] = CustomAuthenticationForm()
        return context

class ContactView(CreateView):
    form_class = ContactForm
    template_name = 'papierbackup/contact.html'
    success_url = reverse_lazy('contact-ok')