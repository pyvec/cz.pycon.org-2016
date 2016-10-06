from django.db import models


class Speaker(models.Model):
    full_name = models.CharField(max_length=200)

    bio = models.TextField(
        help_text="Tell us a bit about yourself! Who you are, where are you"
                  " from, what are your experiences with Python. Be wild,"
                  " be creative!"
    )

    twitter = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    email = models.EmailField(
        help_text="We'll keep it secret, for internal use only."
    )

    photo = models.ImageField(upload_to='speakers/pyconcz2016/')

    talks = models.ManyToManyField('Talk', blank=True)
    workshops = models.ManyToManyField('Workshop', blank=True)

    def __str__(self):
        return self.full_name

    @property
    def copresenters(self):
        return [speaker for speaker in self.talk.speaker_set.all() if speaker != self]


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
        return self.title
