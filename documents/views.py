from django.shortcuts import render
from django.views.generic.list import ListView

from documents.models import Document

class DocumentListView(ListView):
    model = Document