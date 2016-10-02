from django.conf.urls import url

from pyconcz_2016.speakers.views import speakers_list, talks_timeline

urlpatterns = [
    url('^(?P<type>(talks|workshops))$', speakers_list, name="speakers_list"),
    url('^timeline$', talks_timeline, name="talks_timeline"),
]
