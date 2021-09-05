from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField("Category name"), max_length=255)
    created_at = models.DateTimeField("Created date", default=timezone.now)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Body")
    created_at = models.DateTimeField("Created date", default=timezone.now)

    def __str__(self):
        return self.title
    