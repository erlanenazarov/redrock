from __future__ import unicode_literals

from django.db import models

# Create your models here.
from base.models import image_upload_to


class Gallery(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
    image = models.ImageField(upload_to=image_upload_to)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
