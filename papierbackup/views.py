
from django.views.generic.base import TemplateView

from papierbackup.forms import CustomAuthenticationForm

class IndexView(TemplateView):
    template_name = "papierbackup/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['auth_form'] = CustomAuthenticationForm()
        return context

class SubscribeView(FormView):
    pass