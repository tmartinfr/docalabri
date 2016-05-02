from django.conf.urls import url

from documents.views import DocumentListView

urlpatterns = [
    url(r'^', DocumentListView.as_view(), name='document-list'),
]