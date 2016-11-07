from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Race(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=64, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    event_name = models.CharField(max_length=64)

    def __str__(self):
        return self.event_name
