from django.db import migrations

name_map = (
    ('platinum', '1'),
    ('gold', '2'),
    ('silver', '3'),
    ('bronze', '4'),
    ('diversity', '5'),
    ('media', '6'),
)


def rename_choices(apps, schema_editor):
    Sponsor = apps.get_model("sponsors", "Sponsor")

    for before, after in name_map:
        Sponsor.objects.filter(level=before).update(level=after)


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0003_auto_20160908_1412'),
    ]

    operations = [
        migrations.RunPython(rename_choices)
    ]
