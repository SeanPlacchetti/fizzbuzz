__author__ = 'seanplacchetti'
from django.db import models


class FizzBuzz(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=400, blank=True)
    message = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return "(FizzBuzz: " + self.message + ")"
