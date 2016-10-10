from django.conf.urls import url
from django.views.generic import RedirectView

from pyconcz_2016.speakers.views import speakers_list, talks_timeline

urlpatterns = [
    url('^$', RedirectView.as_view(pattern_name='speakers_list'), {'type': 'talks'}),
    url('^(?P<type>(talks|workshops))/$', speakers_list, name="speakers_list"),
    url('^schedule/$', talks_timeline, name="speakers_schedule"),
]
