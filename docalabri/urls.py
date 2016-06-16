from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.views.static import serve

from .views import IndexView, ContactView, RobotsView
from .forms import CustomAuthenticationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^robots.txt$', RobotsView.as_view()),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^contact/ok$', TemplateView.as_view(template_name='docalabri/contact_ok.html'), name='contact-ok'),
    url(r'^login', auth_views.login,
        {'authentication_form': CustomAuthenticationForm, 'template_name': 'docalabri/login.html'}, name='login'),
    url(r'^logout', auth_views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^documents/', include('documents.url')),
]
