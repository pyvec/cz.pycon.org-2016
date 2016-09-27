from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView


prefixed_urlpatterns = [
    url(r'^announcements/', include('pyconcz_2016.announcements.urls')),
    url(r'^proposals/workshops$', RedirectView.as_view(url='/2016/proposals/talks')),
    url(r'^proposals/', include('pyconcz_2016.proposals.urls')),

    url(r'^about/team', include('pyconcz_2016.team.urls')),
    url(r'^speakers/', include('pyconcz_2016.speakers.urls')),

    # static pages
    url(r'^$',
        TemplateView.as_view(template_name='pages/homepage.html'),
        name='homepage'),
    url(r'^about$',
        TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    url(r'^about/code$',
        TemplateView.as_view(template_name='pages/code.html'),
        name='about_code'),
    url(r'^sponsors/offer$',
        TemplateView.as_view(template_name='pages/sponsors_offer.html'),
        name='sponsors_offer'),
]

urlpatterns = (
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
    [
        url(r'^2016/', include(prefixed_urlpatterns)),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^$', RedirectView.as_view(url='/2016/')),
    ]
)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
