from django.db import models


class Speaker(models.Model):
    full_name = models.CharField(max_length=200)
    biography = models.CharField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    github = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='speakers/pyconcz2016/')

    published = models.BooleanField(default=False)
    talk = models.ForeignKey('Talk')

    def __str__(self):
        return self.full_name

    @property
    def copresenters(self):
        return [speaker for speaker in self.talk.speaker_set.all() if speaker != self]


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
