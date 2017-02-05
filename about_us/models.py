from __future__ import unicode_literals

from django.db import models

# Create your models here.
from base.models import image_upload_to


class Resident(models.Model):
    # image = models.ImageField(upload_to=image_upload_to)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Rate(models.Model):
    text = models.TextField()

    def __unicode__(self):
        return self.text
