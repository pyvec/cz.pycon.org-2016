from django.contrib import admin

from .models import Speaker, Talk, Workshop

admin.site.register(Speaker)
admin.site.register(Talk)
admin.site.register(Workshop)
