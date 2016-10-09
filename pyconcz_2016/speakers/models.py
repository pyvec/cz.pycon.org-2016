from django.db import models


class Speaker(models.Model):
    full_name = models.CharField(max_length=200)
    bio = models.TextField()

    twitter = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    email = models.EmailField()

    photo = models.ImageField(upload_to='speakers/pyconcz2016/')

    talks = models.ManyToManyField('Talk', blank=True)
    workshops = models.ManyToManyField('Workshop', blank=True)

    def __str__(self):
        return self.full_name


class Talk(models.Model):
    DIFFICULTY = (
        ('beginner', 'Beginner'),
        ('advanced', 'Advanced'),
    )

    LANGUAGES = (
        ('en', 'English (preferred)'),
        ('cs', 'Czechoslovak'),
    )

    title = models.CharField(max_length=200)
    abstract = models.TextField()

    language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en'
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='beginner',
    )

    def __str__(self):
        return self.title


class Workshop(models.Model):
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

    type = models.CharField(
        max_length=10, choices=TYPE, default='sprint'
    )
    title = models.CharField(
        max_length=200, verbose_name='Title'
    )
    abstract = models.TextField()
    language = models.CharField(
        max_length=2, choices=LANGUAGES, default='en'
    )
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY, default='beginner',
    )
    length = models.CharField(
        max_length=2, choices=LENGTH, blank=True,
    )

    def __str__(self):
        return self.title
