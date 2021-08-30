from django.db import models
from django.utils import timezone

# Create your models here.
class Day(models.Model):
    title = models.CharField("title", max_length=200)
    text = models.TextField("body")
    date = models.DateTimeField("date", default=timezone.now)

    def __str__(self):
        return self.title