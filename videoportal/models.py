from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=25)
    subtitle1 = models.TextField(max_length=25)
    subtitle2 = models.TextField(max_length=25)
    description = models.TextField(max_length=600)
    video_id = models.CharField(max_length=30)
    thumbnail = models.FileField()
    path = models.CharField(max_length=60, blank=True)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)  # todo: auto_now=True

    def __str__(self):
        return self.title
