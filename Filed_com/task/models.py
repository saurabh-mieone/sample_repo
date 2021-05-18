from django.db import models
from django.utils import timezone

# Create your models here.
class song(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, default=" ")
    duration = models.IntegerField(default=0)
    upload_time = models.DateTimeField(default=timezone.now)


class podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10, default=" ")
    duration = models.IntegerField(default=0)
    upload_time = models.DateTimeField(default=timezone.now)
    host = models.CharField(max_length=100, default=" ")
    participants = models.CharField(max_length=111, blank=True, default=" ")


class audiobook(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100, default=" ")
    author = models.CharField(max_length=100, default=" ")
    narrator = models.CharField(max_length=100, default=" ")
    duration = models.IntegerField(default=0)
    upload_time = models.DateTimeField(default=timezone.now)
