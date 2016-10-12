import csv
import sys
from django.core.management import BaseCommand

from pyconcz_2016.speakers.models import Slot, EndTime


def slot2dict(slot):
    shared = {
        'date_start': slot.date,
        'date_end': slot.date_end,

        'room': slot.room,
    }

    if slot.content_object:
        if slot.content_type.model == 'talk':
            speakers = slot.content_object.talks.all()
        else:
            speakers = slot.content_object.workshops.all()

        specific = {
            'type': slot.content_type,
            'title': slot.content_object.title,
            # 'description': slot.content_object.abstract,

            'speaker': ', '.join([speaker.full_name for speaker in speakers]),
            'bio': speakers[0].bio,
            'avatar': 'https://cz.pycon.org' + speakers[0].photo.url,
            'twitter': speakers[0].twitter,
            'github': speakers[0].github,
        }
    else:
        specific = {
            'type': 'event',
            'description': slot.description
        }

    return dict([*shared.items(), *specific.items()])


class Command(BaseCommand):
    def handle(self, *args, **options):
        items = (
            Slot.objects.all()
            .prefetch_related('content_object')
            .annotate(date_end=EndTime())
            .order_by('date', 'room')
        )

        field_names = [
            'date_start', 'date_end',
            'room', 'type',
            'title', 'description',
            'speaker', 'bio', 'avatar', 'twitter', 'github'
        ]
        writer = csv.DictWriter(sys.stdout, fieldnames=field_names)
        writer.writeheader()
        writer.writerows((slot2dict(item) for item in items))



