from django import forms
from django.conf.urls import url
from django.contrib import admin
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db.models import Prefetch
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.utils.html import format_html

from pyconcz_2016.proposals.models import Ranking, Score


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('value', 'note')


class EntryAdmin(admin.ModelAdmin):
    list_display = ['date', 'full_name', 'title', 'score', 'score_link']
    list_display_links = ['title']

    change_list_template = 'admin/proposals/change_list.html'
    change_form_template = 'admin/proposals/change_form.html'

    def score(self, obj):
        try:
            return obj.get_ranking().scores.all()[0]
        except IndexError:
            return None
    score.short_description = 'Your score'

    def score_link(self, obj):
        info = self.model._meta.app_label, self.model._meta.model_name
        url = reverse('admin:%s_%s_add_score' % info, kwargs={'object_id': obj.id})
        return format_html('<a href="{url}">Edit</a>', url=url)
    score_link.short_description = ''

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
                .values_list('object_id', flat=True)
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

        return self.redirect_to_next_unranked(request)

    def add_score(self, request, object_id):
        obj = self.get_queryset(request).get(id=object_id)
        score_instance = (
            obj.get_ranking().scores
                .filter(user=request.user)
                .first()
        )

        if request.method.lower() == 'post':
            score_form = ScoreForm(request.POST, instance=score_instance)
            score_form.instance.user = request.user
            score_form.instance.ranking = obj.get_ranking()

            if score_form.is_valid():
                score_form.save()
                return self.redirect_to_next_unranked(request)

        else:
            score_form = ScoreForm(instance=score_instance)

        ctx = dict(
            self.admin_site.each_context(request),
            obj=obj,
            opts=self.model._meta,
            has_change_permission=self.has_change_permission(request, obj),
            form=self.get_form(request, obj)(instance=obj),
            score_form=score_form
        )

        return TemplateResponse(request, 'admin/proposals/add_score.html', ctx)

    def redirect_to_next_unranked(self, request):
        ct = ContentType.objects.get_for_model(self.model)
        next_obj_id = (
            Ranking.objects
                .filter(content_type=ct)
                .exclude(scores__user=request.user)
                .order_by('?')
                .values_list('object_id', flat=True)
                .first()
        )

        info = self.model._meta.app_label, self.model._meta.model_name

        if next_obj_id:
            return redirect(
                'admin:%s_%s_add_score' % info, object_id=next_obj_id
            )
        else:
            messages.success(request, 'All your work here is done!')
            return redirect('admin:%s_%s_changelist' % info)
