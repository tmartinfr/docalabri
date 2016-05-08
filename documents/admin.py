from django.contrib import admin

from .models import Category, Document, File

class FileInLine(admin.StackedInline):
    model = File

class DocumentAdmin(admin.ModelAdmin):
    inlines = [FileInLine]

admin.site.register(Category)
admin.site.register(Document, DocumentAdmin)
admin.site.register(File)
