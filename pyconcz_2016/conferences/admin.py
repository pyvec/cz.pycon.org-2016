from django.contrib import admin

from pyconcz_2016.conferences.models import Conference


class ConferenceAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_start'
    list_display = ['title', 'edition', 'date_start', 'date_end']
    list_display_links = ['title', 'edition']

admin.site.register(Conference, ConferenceAdmin)
