from django.template.response import TemplateResponse

from pyconcz_2016.speakers.models import Speaker


def homepage(request):
    keynoters = Speaker.objects.filter(keynote=True)

    return TemplateResponse(
        request, 'pages/homepage.html', {'keynoters': keynoters})
