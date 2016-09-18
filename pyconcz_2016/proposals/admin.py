from django.conf.urls import url
from django.contrib import admin
from django.shortcuts import redirect


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'full_name', 'title']
    list_display_links = ['title']

    change_list_template = 'admin/proposals/change_list.html'

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name

        urls = [
            url(
                r'^generate/$',
                self.admin_site.admin_view(self.generate_scoring),
                name='%s_%s_generate' % info
            )
        ]

        return urls + super().get_urls()

    def generate_scoring(self, request):
        """
        Generate Proposal items linked to custom Entries
        """
        context = dict(
            self.admin_site.each_context(request),
        )

        info = self.model._meta.app_label, self.model._meta.model_name

        return redirect('admin:%s_%s_changelist' % info)
