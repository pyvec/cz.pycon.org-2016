from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'full_name', 'title']
    list_display_links = ['title']
