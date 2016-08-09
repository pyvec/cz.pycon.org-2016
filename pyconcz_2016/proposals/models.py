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
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    # Public speaker info
    full_name = models.CharField(
        max_length=200, verbose_name="Your name",
    )
    email = models.EmailField(
        help_text="We'll keep it secret, for internal use only."
    )
    bio = models.TextField(
        help_text="Tell us a bit about yourself! Who you are, where are you"
                  " from, what are your experiences with Python. Be wild,"
                  " be creative!"
    )
    twitter = models.CharField(
        max_length=255, blank=True, verbose_name="Twitter handle (optional)")
    github = models.CharField(
        max_length=255, blank=True, verbose_name="GitHub username (optional)")
    photo = models.ImageField(
        upload_to='proposals/pyconcz2016/talks/', verbose_name="Your picture",
        help_text="Photo of yourself which we can publish on our website"
    )

    # Public talk info
    title = models.CharField(
        max_length=200, verbose_name='Talk title',
        help_text="This is going to be public on all posters! Make up some"
                  " catchy title which attracts audience."
    )
    abstract = models.TextField(
        help_text="Full description of your talk. How would you describe your"
                  "talk to the audience?"
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='beginner',
        help_text="Does you audience require high level of Python knowledge"
                  "or is it suitable for everyone?"
    )

    def __str__(self):
        return '{s.full_name} - {s.title}'.format(s=self)


class Workshop(EntryBase):
    DIFFICULTY = (
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    TYPE = (
        ('sprint', 'Sprint'),
        ('workshop', 'Workshop')
    )

    LENGTH = (
        ('1h', '1 hour'),
        ('2h', '2 hours'),
        ('2h', '3 hours'),
        ('xh', 'Moar!')
    )

    # Public speaker info
    full_name = models.CharField(
        max_length=200, verbose_name="Your name",
    )
    email = models.EmailField(
        help_text="We'll keep it secret, for internal use only."
    )
    bio = models.TextField(
        help_text="Tell us a bit about yourself! Who you are, where are you"
                  " from, what are your experiences with Python. Be wild,"
                  " be creative!"
    )
    twitter = models.CharField(
        max_length=255, blank=True, verbose_name="Twitter handle (optional)")
    github = models.CharField(
        max_length=255, blank=True, verbose_name="GitHub username (optional)")
    photo = models.ImageField(
        upload_to='proposals/pyconcz2016/talks/', verbose_name="Your picture",
        help_text="Photo of yourself which we can publish on our website"
    )

    # Public talk info
    type = models.CharField(
        max_length=10, choices=TYPE, default='sprint',
        help_text="Workshops requires a room, slot in agenda and mandatory "
                  "registration of participants. Sprints requires only table "
                  "to sit around, reliable wifi and dedication to do great "
                  "things!"
    )
    title = models.CharField(
        max_length=200, verbose_name='Workshop/sprint title',
        help_text="Public title. What topic/project is it all about?"
    )
    abstract = models.TextField(
        help_text="Full description of your workshop or sprint. Please also "
                  "describe requirements like installed libraries, Python "
                  "version, etc."
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='beginner',
        help_text="Does you audience require high level of Python knowledge "
                  "or is it suitable for everyone?"
    )
    length = models.CharField(
        max_length=2, choices=LENGTH, blank=True,
        help_text="How much time does your workshop take? Sprints usually take "
                  "whole day, but workshops are organized in smaller blocks. "
                  "You can also have a full-day workshop with lunch break, if "
                  "you want to!"
    )

    def __str__(self):
        return '{s.full_name} - {s.type}/{s.title}'.format(s=self)
