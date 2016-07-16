from django.db import models


class Conference(models.Model):
    title = models.CharField(max_length=100)
    edition = models.CharField(max_length=50)

    date_started = models.DateField()
    date_ended = models.DateField()

    class Meta:
        ordering = ['date_started']

    def __str__(self):
        return '{0} {1}'.format(self.title, self.edition)
