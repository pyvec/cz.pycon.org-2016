from django.conf.urls import url

from pyconcz_2016.speakers.views import speakers_list


urlpatterns = [
    url('^(?P<type>(talks|workshops))$', speakers_list, name="speakers_list"),
]
