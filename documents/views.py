from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Document

class DocumentListView(LoginRequiredMixin, ListView):
    model = Document

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

class DocumentDetailView(LoginRequiredMixin, DetailView):
    model = Document

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)