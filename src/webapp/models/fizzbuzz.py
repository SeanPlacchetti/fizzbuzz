__author__ = 'seanplacchetti'
from django.db import models


class FizzBuzz(models.Model):
    user_agent = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)