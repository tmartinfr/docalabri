from django.contrib import admin

from .forms import FileForm
from .models import Category, Document, File

class FileInLine(admin.StackedInline):
    model = File
    form = FileForm


class DocumentAdmin(admin.ModelAdmin):
    inlines = [FileInLine]

class FileAdmin(admin.ModelAdmin):
    form = FileForm

admin.site.register(Category)
admin.site.register(Document, DocumentAdmin)
admin.site.register(File, FileAdmin)
