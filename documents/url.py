from django.conf.urls import url

from .views import DocumentListView, DocumentDetailView, FileDownload, FilePreview

urlpatterns = [
    url(r'^$', DocumentListView.as_view(), name='document-list'),
    url(r'^(?P<pk>[0-9]+)/?$', DocumentDetailView.as_view(), name='document-detail'),
    url(r'^download/(?P<doc_id>\d+)/(?P<file_id>\d+)/(?P<slug>.+)$',
        FileDownload.as_view(), name='document-download'),
    url(r'^preview/(?P<doc_id>\d+)/(?P<file_id>\d+)/(?P<slug>.+)$',
        FilePreview.as_view(), name='document-preview'),
]
