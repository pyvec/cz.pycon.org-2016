from datetime import datetime

from django.utils.timezone import get_current_timezone

from pyconcz_2016.proposals.models import Talk, Workshop

tz = get_current_timezone()


class TalksConfig:
    model = Talk
    key = 'talks'
    title = 'Talks'
    cfp_title = 'Submit your talk'
    template_about = 'proposals/talks_about.html'
    date_start = datetime(year=2016, month=8, day=1, hour=12, minute=0, tzinfo=tz)
    date_end = datetime(year=2016, month=9, day=12, hour=12, minute=0, tzinfo=tz)


class WorkshopsConfig:
    model = Workshop
    key = 'workshops'
    title = 'Workshops'
    cfp_title = 'Submit your workshop'
    template_about = 'proposals/workshops_about.html'
    date_start = datetime(year=2016, month=8, day=1, hour=12, minute=0, tzinfo=tz)
    date_end = datetime(year=2016, month=10, day=5, hour=12, minute=0, tzinfo=tz)
