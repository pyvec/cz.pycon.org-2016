from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.db.models import Prefetch
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from pyconcz_2016.proposals.models import Ranking, Score


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('value', 'note')


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'full_name', 'title', 'score']
    list_display_links = ['title']

    change_list_template = 'admin/proposals/change_list.html'
    change_form_template = 'admin/proposals/change_form.html'

    def score(self, obj):
        return obj.get_ranking().scores.all().first()
    score.short_description = 'Your score'

    def get_queryset(self, request):
        scores = Prefetch(
            'rankings__scores',
            queryset=Score.objects.filter(user=request.user)
        )
        return super().get_queryset(request).prefetch_related(scores)

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name

        urls = [
            url(
                r'^generate/$',
                self.admin_site.admin_view(self.generate_scoring),
                name='%s_%s_generate' % info
            ),
            url(
                r'^(?P<object_id>\d+)/add_score/$',
                self.admin_site.admin_view(self.add_score),
                name='%s_%s_add_score' % info
            )
        ]

        return urls + super().get_urls()

    def generate_scoring(self, request):
        """
        Generate empty Rankings linked to custom Entries
        """

        ct = ContentType.objects.get_for_model(self.model)
        existing_ids = (
            Ranking.objects
                .filter(content_type=ct)
                .values_list('id', flat=True)
        )

        proposals = (
            Ranking(content_type=ct, object_id=oid) for oid in
            self.model.objects
                .exclude(id__in=existing_ids)
                .values_list('id', flat=True)
        )

        objs = Ranking.objects.bulk_create(proposals)

        obj_count = len(objs)
        if obj_count:
            msg = "{} new proposals available for scoring"
            messages.success(request, msg.format(obj_count))
        else:
            messages.info(request, "No new proposals available for scoring")

        info = self.model._meta.app_label, self.model._meta.model_name
        return redirect('admin:%s_%s_changelist' % info)

    def add_score(self, request, object_id):
        obj = self.get_queryset(request).get(id=object_id)

        if request.method.lower() == 'post':
            score_form = ScoreForm(request.POST)
            score_form.instance.user = request.user
            score_form.instance.ranking = obj.get_ranking()

            if score_form.is_valid():
                score_form.save()

                next_obj = (
                    # Go to random next unranked item
                    self.get_queryset(request)
                        .filter(rankings__scores__value=None)
                        .order_by('?')
                        .first()
                )

                info = self.model._meta.app_label, self.model._meta.model_name

                if next_obj:
                    return redirect(
                        'admin:%s_%s_add_score' % info, object_id=next_obj.id
                    )
                else:
                    messages.success(request, 'All your work here is done!')
                    return redirect('admin:%s_%s_changelist' % info)

        else:
            score_form = ScoreForm()

        ctx = dict(
            self.admin_site.each_context(request),
            obj=obj,
            opts=self.model._meta,
            has_change_permission=self.has_change_permission(request, obj),
            form=self.get_form(request, obj)(instance=obj),
            score_form=score_form
        )

        return TemplateResponse(request, 'admin/proposals/add_score.html', ctx)
