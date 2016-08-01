from datetime import datetime

from django.utils.timezone import get_current_timezone

from pyconcz_2016.proposals.models import Talk, Workshop

tz = get_current_timezone()


class TalksConfig:
    model = Talk
    key = 'talks'
    title = 'Talks'
    template_about = 'proposals/talks_about.html'
    date_start = datetime(year=2016, month=8, day=1, hour=12, minute=0, tzinfo=tz)
    date_end = datetime(year=2016, month=9, day=7, hour=12, minute=0, tzinfo=tz)


class WorkshopsConfig:
    model = Workshop
    key = 'workshops'
    title = 'Workshops'
    template_about = 'proposals/workshops_about.html'
    date_start = datetime(year=2016, month=8, day=1, hour=12, minute=0, tzinfo=tz)
    date_end = datetime(year=2016, month=10, day=5, hour=12, minute=0, tzinfo=tz)
