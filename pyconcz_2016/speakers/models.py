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

    talks = models.ManyToManyField('Talk')

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
