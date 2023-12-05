from django.contrib import admin
from .models import (
    HTML_CSS,
    JS,
    PY,
    DJ,
    Comment,
)

admin.site.register(HTML_CSS)
admin.site.register(JS)
admin.site.register(PY)
admin.site.register(DJ)
admin.site.register(Comment)
