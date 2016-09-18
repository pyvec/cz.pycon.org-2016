from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from pyconcz_2016.proposals.models import Proposal


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

        ct = ContentType.objects.get_for_model(self.model)
        existing_ids = (
            Proposal.objects
                .filter(content_type=ct)
                .values_list('id', flat=True)
        )

        proposals = (
            Proposal(content_type=ct, object_id=oid) for oid in
            self.model.objects
                .exclude(id__in=existing_ids)
                .values_list('id', flat=True)
        )

        objs = Proposal.objects.bulk_create(proposals)

        obj_count = len(objs)
        if obj_count:
            msg = "{} new proposals available for scoring"
            messages.success(request, msg.format(obj_count))
        else:
            messages.info(request, "No new proposals available for scoring")

        return redirect('admin:%s_%s_changelist' % info)
