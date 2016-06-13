import os.path
import mimetypes

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View

import logging

from .models import Document, File

logger = logging.getLogger(__name__)


class DocumentListView(LoginRequiredMixin, ListView):
    model = Document

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)


class DocumentDetailView(LoginRequiredMixin, DetailView):
    model = Document

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)


class FileBaseDownload(LoginRequiredMixin, View):
    def _get(self, request, doc_id, file_id, slug, download=True):
        doc = Document.objects.get(user=self.request.user, pk=doc_id)
        if not doc:
            logger.warning(
                "Unauthorized acces by user {} to [doc:%s]".format(
                    self.request.user, doc)
            )
            raise PermissionDenied()

        f = File.objects.get(pk=file_id, document=doc)
        if not f:
            logger.warning(
                "Unauthorized acces by user {} to [doc:%s][file:%s]".format(
                    self.request.user, doc, f)
            )
            raise PermissionDenied()

        logger.debug("Accessing [doc:%s][file:%s]" % (doc, f))
        response = HttpResponse()
        mimetype = mimetypes.guess_type(f.file.url)
        response['Content-Type'] = mimetype[0]
        if download:
            name = f.file.url.split('/')[-1]
            response['Content-Disposition'] = \
                'attachment; filename={}-{}'.format(slugify(doc), name)

        redir = f.file.url.replace(settings.MEDIA_URL, settings.PRIVATE_URL, 1)
        response['X-Accel-Redirect'] = redir
        logger.debug(response)
        return response


class FilePreview(FileBaseDownload):
    """ This view interacts with Nginx to serve files efficiently
        by using x-accel-redirect feature.
    """

    def get(self, request, doc_id, file_id, slug):
        return self._get(request, doc_id, file_id, slug, False)


class FileDownload(FileBaseDownload):
    """ This view interacts with Nginx to serve files efficiently
        by using x-accel-redirect feature.

    """

    def get(self, request, doc_id, file_id, slug):
        return self._get(request, doc_id, file_id, slug)
