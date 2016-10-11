import datetime
from django import template

register = template.Library()


@register.filter
def day_type(value):
    date = value.date()
    if date == datetime.date(year=2016, month=10, day=30):
        return 'workshops'
    elif date in [datetime.date(year=2016, month=10, day=28 + i) for i in range(2)]:
        return 'talks'
