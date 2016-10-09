import csv

from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from pyconcz_2016.speakers.models import Slot, Talk


def get_talk(title):
    try:
        return Talk.objects.get(title__iexact=title)
    except Talk.DoesNotExist:
        print('Not found ', title)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['csv_file']:
            Slot.objects.bulk_create(self.read_talks(filename))

    def read_talks(self, filename):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')

            (day, *_) = next(reader)
            rooms = ['d105', 'd0206', 'd0207']

            for (time, _, track1, track2, track3) in reader:
                date = datetime.strptime(" ".join([day, time]),
                                         '%Y-%m-%d %I:%M:%S %p')
                date = timezone.make_aware(date, timezone.get_current_timezone())

                if not track2 or not track3 or track1.endswith('Break'):
                    yield Slot(date=date, description=track1, room='foyer')
                else:
                    talks = [get_talk(title)
                             for title in [track1, track2, track3]]
                    yield from (Slot(date=date, talk=talk, room=room)
                                for (talk, room) in zip(talks, rooms))
