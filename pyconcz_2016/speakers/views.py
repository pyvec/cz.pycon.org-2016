from django.template import RequestContext
from django.template.response import TemplateResponse

from pyconcz_2016.speakers.models import Speaker, Slot


def speakers_list(request, type):
    speakers = (Speaker.objects.all()
                .exclude(**{type: None})
                .prefetch_related(type)
                .order_by('full_name'))

    return TemplateResponse(
        request,
        template='speakers/{}_list.html'.format(type),
        context={'speakers': speakers}
    )


def talks_timeline(request):
    talks = (Slot.objects.all()
                .select_related('talk')
                .prefetch_related('talk__speakers')
                .order_by('date'))

    return TemplateResponse(
        request,
        template='speakers/talks_timeline.html',
        context={
            'talks': talks
        }
    )
