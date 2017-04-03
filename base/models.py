# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from redactor.fields import RedactorField


def image_upload_to(instance, filename):
    return "images/%s" % filename


class Category(models.Model):
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to=image_upload_to)

    def __unicode__(self):
        return self.name


class Tour(models.Model):
    class Meta:
        verbose_name = 'tour'
        verbose_name_plural = 'Tours'

    title = models.CharField(max_length=1000)
    short_description = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_to)
    text = RedactorField(verbose_name='Текст',
                         upload_to=image_upload_to,
                         allow_image_upload=True,
                         allow_file_upload=True)
    pdf = models.FileField(upload_to=image_upload_to, null=True, blank=True)
    down = models.BooleanField(default=True)
    initial = models.DateField()
    final = models.DateField()
    days = models.IntegerField(default=1)
    category = models.ForeignKey(Category)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'Comments'

    tour = models.ForeignKey(Tour)
    author = models.CharField(max_length=100, default="Anonymous")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __unicode__(self):
        return self.author
