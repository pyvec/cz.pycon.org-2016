from django.contrib import admin

from pyconcz_2016.sponsors.models import Sponsor


class SponsorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sponsor, SponsorAdmin)
