from django.contrib import admin

from pyconcz_2016.conferences.models import Conference


class ConferenceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_started'
    list_display = ['title', 'edition', 'date_started', 'date_ended']
    list_display_links = ['title', 'edition']

admin.site.register(Conference, ConferenceAdmin)
