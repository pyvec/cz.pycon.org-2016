from django.db.models import Case
from django.db.models import IntegerField
from django.db.models import Value
from django.db.models import When
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


def schedule(request):
    slots = (Slot.objects.all()
                .prefetch_related('content_object', 'content_object__speakers')
                .annotate(order=Case(
                    When(room='d105', then=Value(1)),
                    When(room='d0206', then=Value(2)),
                    When(room='d0207', then=Value(3)),
                    When(room='a112', then=Value(4)),
                    When(room='a113', then=Value(5)),
                    default=Value(0),
                    output_field=IntegerField()
                ))
                .order_by('date', 'order'))

    return TemplateResponse(
        request,
        template='speakers/slot_schedule.html',
        context={
            'slots': slots
        }
    )
