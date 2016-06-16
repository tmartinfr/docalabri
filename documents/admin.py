from django.contrib import admin

from .forms import FileForm
from .models import Category, Document, File


class FileInLine(admin.StackedInline):
    model = File
    form = FileForm


class DocumentAdmin(admin.ModelAdmin):
    inlines = [FileInLine]
    list_filter = ('user__username', 'category')


class FileAdmin(admin.ModelAdmin):
    model = File
    list_filter = ('document__user__username', 'document__name')


class FileAdmin(admin.ModelAdmin):
    form = FileForm

admin.site.register(Category)
admin.site.register(Document, DocumentAdmin)
admin.site.register(File, FileAdmin)
