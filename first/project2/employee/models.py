from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField("Dep Name", max_length=20)
    created_at = models.DateTimeField("Date", default=timezone.now)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField("First name", max_length=20)
    last_name = models.CharField("Last name", max_length=20)
    email = models.EmailField("E-mail", max_length=254, blank=True)
    department = models.ForeignKey(
        Department, verbose_name="Dep Name", on_delete=models.PROTECT
    )
    