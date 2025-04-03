from django.contrib import admin

from .models import Files, Folder

admin.site.register(Folder)
admin.site.register(Files)
