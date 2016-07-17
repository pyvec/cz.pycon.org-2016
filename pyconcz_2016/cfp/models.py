from django.db import models
from django.utils.timezone import now

from pyconcz_2016.conferences.models import Conference


class Cfp(models.Model):
    conference = models.ForeignKey(Conference, related_name="cfps")
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    date_start = models.DateTimeField()
    date_end = models.DateTimeField()

    class Meta:
        ordering = ['date_start']

    def __str__(self):
        return self.title


class Proposal(models.Model):
    DIFFICULTY = (
        ('all', 'All'),
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    cfp = models.ForeignKey(Cfp, related_name='proposals')

    # Public speaker info
    full_name = models.CharField(max_length=200)
    bio = models.TextField()
    twitter = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)

    # Public talk info
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='all')

    # Private notes (for reviewers only)
    note = models.TextField()
    date = models.DateTimeField(default=now)
