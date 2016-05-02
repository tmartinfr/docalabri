from django.conf.urls import url

from documents.views import DocumentListView, DocumentDetailView

urlpatterns = [
    url(r'^$', DocumentListView.as_view(), name='document-list'),
    url(r'^(?P<pk>[0-9]+)$', DocumentDetailView.as_view(), name='document-detail'),
]