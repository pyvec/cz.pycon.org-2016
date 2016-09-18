from django.template import RequestContext
from django.template.response import TemplateResponse

from pyconcz_2016.speakers.models import Speaker


def speakers_list(request):
    speakers = Speaker.objects.all().filter(published=True).select_related('talk').order_by('?')

    return TemplateResponse(
        request,
        template='speakers/speakers_list.html',
        context={
            'speakers': speakers
        }
    )
