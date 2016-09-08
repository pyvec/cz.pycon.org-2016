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

    LANGUAGES = (
        ('en', 'English (preferred)'),
        ('cs', 'Czechoslovak'),
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
        max_length=255, blank=True,
        verbose_name="Twitter handle", help_text="Optional")
    github = models.CharField(
        max_length=255, blank=True,
        verbose_name="GitHub username", help_text="Optional")
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
    language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en'
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
        ('workshop', 'Workshop'),
        ('sprint', 'Sprint'),
    )

    LENGTH = (
        ('1h', '1 hour'),
        ('2h', '2 hours'),
        ('2h', '3 hours'),
        ('1d', 'Full day (most sprints go here!)'),
        ('xx', 'Something else! (Please leave a note in the abstract!)')
    )

    LANGUAGES = (
        ('en', 'English (preferred)'),
        ('cs', 'Czech/Slovak'),
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
        max_length=255, blank=True,
        verbose_name="Twitter handle", help_text="Optional")
    github = models.CharField(
        max_length=255, blank=True,
        verbose_name="GitHub username", help_text="Optional")
    photo = models.ImageField(
        upload_to='proposals/pyconcz2016/talks/', verbose_name="Your picture",
        help_text="Photo of yourself which we can publish on our website"
    )

    # Public talk info
    type = models.CharField(
        max_length=10, choices=TYPE, default='sprint',
        help_text="At a workshop, you should present hands-on excercises for"
                  " participants to learn from. You'll get a room and a slot"
                  " in the agenda, and participants will need to register.\n"
                  " At a sprint, participants help an open-source project --"
                  " usually by cloning the repo and trying to fix"
                  " beginner-level issues, while you'll provide one-to-one"
                  " mentorship. If several experienced developers"
                  " are around, sprints are also a good place for serious"
                  " design discussions. Sprinters only need a table to sit"
                  " around, reliable wifi, and dedication to do great things!"
    )
    title = models.CharField(
        max_length=200, verbose_name='Workshop/sprint title',
        help_text="Public title. What topic/project is it all about?"
    )
    abstract = models.TextField(
        help_text="Full description of your workshop or sprint. Please also"
                  " describe requirements: libraries and Python version to be"
                  " installed, required experience with topics/libraries, etc."
    )
    language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en'
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='beginner',
        help_text="Does you audience require high level of specialized"
                  " knowledge (of Python, a library, etc.),"
                  " or is it suitable for everyone?"
    )
    length = models.CharField(
        max_length=2, choices=LENGTH, blank=True,
        help_text="How much time does your workshop take? Sprints usually take"
                  " the whole day, but workshops are organized in smaller"
                  " blocks. You can also have a full-day workshop with lunch"
                  " break, but keep in mind that the length could discourage"
                  " attendees!"
    )

    def __str__(self):
        return '{s.full_name} - {s.type}/{s.title}'.format(s=self)


class FinancialAid(EntryBase):
    # Public speaker info
    full_name = models.CharField(
        max_length=200, verbose_name="Your name",
    )
    email = models.EmailField(
        help_text="We'll keep it secret, for internal use only."
    )
    bio = models.TextField(
        help_text="Tell us a bit about yourself! Who you are, where are you"
                  " from, what are your experiences with Python. Also include"
                  " how are you involved in Python community and how do you"
                  " contribute or do you plan to contribute to community."
    )
    amount = models.CharField(
        max_length=255,
        help_text="How much money would you like to get"
                  " (please specify currency)."
    )

    purpose = models.TextField(
        help_text="How would you like to use granted money?"
    )

    def __str__(self):
        return self.full_name

    # required for generic admin
    def title(self):
        return self.full_name
