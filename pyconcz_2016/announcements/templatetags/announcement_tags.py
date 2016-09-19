from django import template

from pyconcz_2016.announcements.models import Announcement

register = template.Library()


@register.inclusion_tag('announcements/latest.html')
def latest_announcement():
    return {'item': Announcement.objects.all().latest()}
