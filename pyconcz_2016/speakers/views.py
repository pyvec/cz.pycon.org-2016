from django.template import RequestContext
from django.template.response import TemplateResponse

from pyconcz_2016.speakers.models import Speaker


def speakers_list(request):
    speakers = (Speaker.objects.all()
                .prefetch_related('talks')
                .order_by('full_name'))

    return TemplateResponse(
        request,
        template='speakers/speakers_list.html',
        context={
            'speakers': speakers
        }
    )
