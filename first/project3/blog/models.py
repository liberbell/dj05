from django.db import models
from django.urls import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField("Title", max_length=255)