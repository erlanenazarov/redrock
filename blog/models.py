# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from redactor.fields import RedactorField

from base.models import image_upload_to


class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = RedactorField(
        verbose_name='Текст',
        allow_image_upload=False,
        allow_file_upload=False
    )

    def __unicode__(self):
        return self.title

    def get_image(self):
        try:
            image = Images.objects.filter(blog=self)[0]
            return image
        except:
            pass


class Images(models.Model):
    blog = models.ForeignKey(Blog)
    image = models.ImageField(upload_to=image_upload_to)


class Comment(models.Model):
    author = models.CharField(max_length=100, default='Anonymous')
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.author
