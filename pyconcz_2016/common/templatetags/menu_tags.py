from django import template
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def show_menu(context):
    menu_items = [
        {
            'path': '/2016/',
            'icon': 'fa-home',
            'title': 'Homepage',
        }, {
            'path': reverse('about'),
            'title': 'Event',
            'menu': [
                {
                    'path': reverse('about'),
                    'title': 'About'
                }, {
                    'path': reverse('team_list'),
                    'title': 'Team'
                }, {
                    'path': reverse('sponsors_list'),
                    'title': 'Sponsors'
                }, {
                    'path': reverse('about_code'),
                    'title': 'Code of Conduct'
                },
            ]
        }, {
            'path': reverse('about_brno'),
            'title': 'Brno',
            'menu': [
                {
                    'path': reverse('about_brno'),
                    'title': 'Guide',
                }, {
                    'path': reverse('about_brno') + "#how-to-get-to-brno",
                    'title': 'Travelling',
                }, {
                    'path': reverse('about_brno') + "#accommodation-tips",
                    'title': 'Accommodation',
                },
            ]
        }, {
            'path': reverse('speakers_schedule'),
            'title': 'Program',
            'menu': [
                {
                    'path': reverse('speakers_schedule'),
                    'title': 'Schedule',
                }, {
                    'path': reverse('speakers_list', kwargs={'type': 'talks'}),
                    'title': 'Speakers',
                }, {
                    'path': reverse('speakers_list', kwargs={'type': 'workshops'}),
                    'title': 'Workshops',
                },
            ]
        }, {
            'path': 'https://ti.to/pyvec/pycon-cz-2016',
            'title': 'Tickets',
            'highlight': True
        }
    ]

    path = context['request'].path

    for root in menu_items:
        if 'menu' not in root:
            continue

        for child in root['menu']:
            if child['path'] == path:
                root['selected'] = child['selected'] = True

    return {
        'menu_items': menu_items
    }
