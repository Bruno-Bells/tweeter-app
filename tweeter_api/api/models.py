from django.db import models
import json
from django.utils import timezone
import jsonfield
from djongo.models.fields import ObjectIdField


# Create your models here.

class Tweet(models.Model):
    _id = ObjectIdField()
    status = models.BooleanField()
    message = models.CharField(max_length=100)
    data = jsonfield.JSONField()
    created = models.DateTimeField('date created', default=timezone.now)


class Handle(models.Model):
    _id = ObjectIdField()
    username = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.username

class Interval(models.Model):
    _id = ObjectIdField()
    interval = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.interval
