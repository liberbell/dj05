from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Body")
    created_at = models.DateTimeField("Created date", default=timezone.now)