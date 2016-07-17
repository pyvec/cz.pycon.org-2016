from django.conf.urls import url

from pyconcz_2016.cfp.views import proposal_success, proposal_create

slug_re = r'(?P<slug>[^/]*)'

urlpatterns = [
    url('^{}/sent$'.format(slug_re), proposal_success, name='cfp_success'),
    url('^{}$'.format(slug_re), proposal_create, name='cfp_form'),
]
