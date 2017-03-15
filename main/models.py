from __future__ import unicode_literals

from django.db import models

# Create your models here.
from base.models import image_upload_to, Tour


class Slider(models.Model):
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Slider Images'
        ordering = '-created_at'.split()

    image = models.ImageField(upload_to=image_upload_to)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.title


class Main(models.Model):
    class Meta:
        verbose_name = 'Information'
        verbose_name_plural = 'Main information'
        ordering = '-created_at'.split()

    image = models.ImageField(upload_to=image_upload_to)
    description = models.TextField()
    url = models.URLField(max_length=10000)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.description[0:20] + '...'


class ThingsToDo(models.Model):
    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'THINGS TO DO'

    name = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to=image_upload_to)
    tours = models.ManyToManyField(Tour)

    def __unicode__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_to)
    link = models.URLField(max_length=10000)

    def __unicode__(self):
        return self.name


class TripPlanner(models.Model):
    class Meta:
        verbose_name = 'TRIP PLANNER'
        verbose_name_plural = 'Trip Planner'

    choices = (
        ('Luxe', 'Luxe'),
        ('Standart', 'Standart'),
        ('Budget', 'Budget'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    comment = models.TextField(null=True, blank=True)
    initial = models.DateField()
    final = models.DateField()
    people = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    tour = models.ForeignKey(Tour, null=True, blank=True)
    category_of_tour = models.CharField(max_length=100, choices=choices, null=True, blank=True)
    hotel = models.ForeignKey(Hotel, null=True, blank=True)
    transport_choices = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    food_choices = (
        ('Full board', 'Full board'),
        ('Half board', 'Half board'),
        ('Bed breakfast', 'Bed breakfast'),
        ('Room only', 'Room only'),
    )
    transport = models.CharField(max_length=100, choices=transport_choices, null=True, blank=True)
    food = models.CharField(max_length=100, choices=food_choices, null=True, blank=True)

    def __unicode__(self):
        return self.name


class FAQ(models.Model):
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
    phone = models.CharField(null=True, blank=True, max_length=100)
    email = models.CharField(null=True, blank=True, max_length=100)
    text = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.email
