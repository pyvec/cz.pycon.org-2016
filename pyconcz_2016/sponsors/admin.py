from django.contrib import admin
from django.utils.html import format_html

from pyconcz_2016.sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'get_link', 'published']
    list_display_links = ['name']

    def get_link(self, instance):
        return format_html("<a href='{url}'>{url}</a>", url=instance.link_url)


admin.site.register(Sponsor, SponsorAdmin)
