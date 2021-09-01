from django.db import models
from django.db.models.fields import DateTimeField
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField("Dep Name", max_length=20)
    created_at = models.DateTimeField("Date", default=timezone.now)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField("Club Name", max_length=20)
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
    club = models.ManyToManyField(Club, verbose_name="Club Name")
    created_at = models.DateTimeField("Date", default=timezone.now)

    def __str__(self):
        return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)