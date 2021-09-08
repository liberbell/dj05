from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField("Category name", max_length=255)
    created_at = models.DateTimeField("Created date", default=timezone.now)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Body")
    created_at = models.DateTimeField("Created date", default=timezone.now)

    category = models.ForeignKey(Category, verbose_name="Category name", on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    name = models.CharField("Name", max_length=50, default="nemo")
    text = models.TextField("Text")
    post = models.ForeignKey(Post, verbose_name=("Articles"), on_delete=models.PROTECT)
    created_at = models.DateTimeField("Created date", default=timezone.now)