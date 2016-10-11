from django.contrib import admin
from .models import Speaker, Talk, Slot, Workshop


class SlotAdmin(admin.ModelAdmin):
    list_display = ['date', 'get_description', 'room']
    list_filter = ['room']
    date_hierarchy = 'date'

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('content_object')

    def get_description(self, obj):
        return obj.content_object or obj.description


admin.site.register(Speaker)
admin.site.register(Talk)
admin.site.register(Workshop)
admin.site.register(Slot, SlotAdmin)
