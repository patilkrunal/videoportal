from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    video_id = models.CharField(max_length=30)
    path = models.CharField(max_length=60, blank=True)
    datetime = models.DateTimeField(auto_now=True, blank=False, null=False)  # todo: auto_now=True

    def __str__(self):
        return self.title
