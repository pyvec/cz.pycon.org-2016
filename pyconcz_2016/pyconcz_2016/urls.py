from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView


prefixed_urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='pages/homepage.html')),
    url(r'^about/cfp', TemplateView.as_view(template_name='pages/cfp.html')),
    url(r'^about/code', TemplateView.as_view(template_name='pages/code.html')),
    url(r'^sponsors/offer', TemplateView.as_view(template_name='pages/sponsors_offer.html')),
]

urlpatterns = [
    url(r'^2016/', include(prefixed_urlpatterns)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url='/2016/'))
]
