from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Runner(models.Model):
    curr_year = date.today().year
    GRAD_YEAR = [(i,i) for i in range(curr_year+1,curr_year+5)]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=64, null=True, blank=True)
    gradyear = models.IntegerField(choices=GRAD_YEAR)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
