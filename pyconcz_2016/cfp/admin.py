from django.contrib import admin

from pyconcz_2016.cfp.models import Cfp, Proposal


class CfpAdmin(admin.ModelAdmin):
    list_display = ['conference', 'title', 'date_start', 'date_end']
    list_display_links = ['title']


class ProposalAdmin(admin.ModelAdmin):
    list_display = ['cfp', 'full_name', 'title']
    list_display_links = ['title']
    list_filter = ['cfp']


admin.site.register(Cfp, CfpAdmin)
admin.site.register(Proposal, ProposalAdmin)
