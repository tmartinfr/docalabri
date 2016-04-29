
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm

class IndexView(TemplateView):
    template_name = "papierbackup/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        auth_form = AuthenticationForm()

        # Add CSS class used by Bootstrap.
        auth_form.fields['username'].widget.attrs.update({'class': 'form-control'})
        auth_form.fields['password'].widget.attrs.update({'class': 'form-control'})

        context['auth_form'] = auth_form
        return context