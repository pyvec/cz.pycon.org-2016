from django.db import models


class Announcement(models.Model):
    message = models.TextField()
    link = models.URLField(blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        get_latest_by = 'date_created'
        ordering = ['-date_created']

    def __str__(self):
        if len(self.message) > 30:
            return self.message[:30] + '…'
        else:
            return self.message
