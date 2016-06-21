import os
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseForbidden
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


class FileBaseDownload(View):
    """ This view interacts with Nginx to serve files efficiently
        by using x-accel-redirect feature.
    """
    def _get(self, request, file_id, slug, download=True):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        try:
            f = File.objects.select_related('document').get(pk=file_id, document__user=request.user)
        except ObjectDoesNotExist:
            logger.warning("Unauthorized access by user {} to [file:{}]".format(request.user, file_id))
            return HttpResponseForbidden()

        logger.debug("Accessing [file:%s]" % (f))

        response = HttpResponse()
        response['Content-Type'] = f.mimetype

        if download:
            response['Content-Disposition'] = 'attachment; filename={}'.format(f.slugname)

        if settings.DEBUG:
            file_location = os.path.join(settings.MEDIA_ROOT, f.file.url)
            response.write(open(file_location).read())
        else:
            redir = f.file.url.replace(settings.MEDIA_URL, settings.PRIVATE_URL, 1)
            response['X-Accel-Redirect'] = redir
            logger.debug(response)

        return response


class FilePreview(FileBaseDownload):

    def get(self, request, file_id, slug):
        return self._get(request, file_id, slug, download=False)


class FileDownload(FileBaseDownload):

    def get(self, request, file_id, slug):
        return self._get(request, file_id, slug)
