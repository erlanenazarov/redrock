from django.contrib import admin

# Register your models here.
from media.models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    list_display = 'name author icon'.split()
    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True
admin.site.register(Gallery, GalleryAdmin)