from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User, Group

from main.models import Slider, Main, ThingsToDo, TripPlanner, Hotel

admin.site.unregister(User)
admin.site.unregister(Group)


class SliderAdmin(admin.ModelAdmin):
    list_display = 'title icon'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True


admin.site.register(Slider, SliderAdmin)


class MainAdmin(admin.ModelAdmin):
    list_display = 'icon url'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True


admin.site.register(Main, MainAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display = 'name icon link'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True


admin.site.register(Hotel, HotelAdmin)


class TripPlannaerAdmin(admin.ModelAdmin):
    list_display = 'name country phone people children'.split()


admin.site.register(TripPlanner, TripPlannaerAdmin)


class ThingsToDoAdmin(admin.ModelAdmin):
    list_display = 'name icon'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True


admin.site.register(ThingsToDo, ThingsToDoAdmin)
