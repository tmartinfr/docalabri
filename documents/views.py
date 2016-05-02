from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from documents.models import Document

class DocumentListView(ListView):
    model = Document

class DocumentDetailView(DetailView):
    model = Document