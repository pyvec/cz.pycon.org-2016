from django.template import RequestContext
from django.template.response import TemplateResponse

from pyconcz_2016.speakers.models import Speaker


def speakers_list(request, type):
    speakers = (Speaker.objects.all()
                .exclude(**{type: None})
                .prefetch_related(type)
                .order_by('full_name'))

    return TemplateResponse(
        request,
        template='speakers/speakers_list.html',
        context={
            'speakers': speakers,
            'show_talks': type == 'talks',
            'show_workshops': type == 'workshops'
        }
    )
