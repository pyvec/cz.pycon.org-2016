from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.timezone import now


class Proposal(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class EntryBase(models.Model):
    # Private notes (for reviewers only)
    note = models.TextField()
    date = models.DateTimeField(default=now)

    class Meta:
        abstract = True


class Talk(EntryBase):
    DIFFICULTY = (
        ('all', 'All'),
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    # Public speaker info
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    twitter = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)

    # Public talk info
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='all')

    def __str__(self):
        return '{s.full_name} - {s.title}'.format(s=self)


class Workshop(EntryBase):
    DIFFICULTY = (
        ('all', 'All'),
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    # Public speaker info
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    bio = models.TextField()
    twitter = models.CharField(max_length=20, blank=True)
    github = models.CharField(max_length=20, blank=True)

    # Public talk info
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='all')

    def __str__(self):
        return '{s.full_name} - {s.title}'.format(s=self)


# FIXME: What fields to include?
# class FinancialAide(models.Model):
#     # Public speaker info
#     full_name = models.CharField(max_length=200)
#     email = models.EmailField()
#     bio = models.TextField()
