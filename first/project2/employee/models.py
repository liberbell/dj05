from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField("Dep Name", max_length=20)
    created_at = models.DateTimeField("Date", default=timezone.now)