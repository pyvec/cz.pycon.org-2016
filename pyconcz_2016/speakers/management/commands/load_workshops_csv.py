import csv

from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from pyconcz_2016.speakers.models import Slot, Workshop


def get_workshop(title):
    try:
        return Workshop.objects.get(title__iexact=title)
    except Workshop.DoesNotExist:
        print('Not found ', title)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['csv_file']:
            Slot.objects.bulk_create(self.read_workshops(filename))

    def read_workshops(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            for (time, room, speaker, title) in reader:
                date = datetime.strptime(" ".join(['2016-10-30', time]),
                                         '%Y-%m-%d %H:%M')
                date = timezone.make_aware(date, timezone.get_current_timezone())

                if not title:
                    yield Slot(date=date, description=speaker, room=room)
                else:
                    workshop = get_workshop(title)
                    yield Slot(date=date, content_object=workshop, room=room)
