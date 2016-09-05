from django.db import models


class Sponsor(models.Model):
    LEVEL = (
        ('platinum', 'Platinum'),
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
    )

    level = models.CharField(max_length=20, choices=LEVEL, default='bronze')

    name = models.CharField(max_length=200)
    logo = models.FileField(upload_to='sponsors/pyconcz_2016/')

    description = models.TextField()
    link_url = models.URLField()

    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["level", "name"]

    def __str__(self):
        return self.name
