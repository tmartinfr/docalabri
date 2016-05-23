
import mimetypes

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def document_preview(value):
    ret = ''
    _mimetype = mimetypes.guess_type(value)[0]
    if(_mimetype):
        if(_mimetype.partition('/')[0] == 'image'):
            ret = '<img src="{}" width="600">'.format(value)
        elif(_mimetype == 'application/pdf'):
            ret = '<iframe src="{}" width="600" height="300"></iframe>'.format(value)
    return mark_safe(ret)
