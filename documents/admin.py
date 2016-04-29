from django.contrib import admin

from .models import Document, File

class FileInLine(admin.StackedInline):
    model = File

class DocumentAdmin(admin.ModelAdmin):
    inlines = [FileInLine]

admin.site.register(Document, DocumentAdmin)
admin.site.register(File)