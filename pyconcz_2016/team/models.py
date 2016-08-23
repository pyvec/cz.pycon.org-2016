from django.db import models


class Organizer(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(
        default='', blank=True,
        help_text="This is private")
    bio = models.TextField()
    twitter = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='team/pyconcz2016/')

    published = models.BooleanField(default=False)
