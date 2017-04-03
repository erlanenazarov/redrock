from django.contrib import admin

# Register your models here.
from blog.models import Blog, Images, Comment


class ImageInline(admin.StackedInline):
    model = Images
    extra = 1


class BlogAdmin(admin.ModelAdmin):
    list_display = 'title'.split()
    # def icon(self, obj):
    #     try:
    #         img = obj.get_image
    #         return '<img src="%s" style = "width:50px; height=50px;" />' % img.url
    #     except:
    #         return '<p>No Cover</p>'
    #
    # icon.allow_tags = True
    inlines = [ImageInline]

admin.site.register(Comment)
admin.site.register(Blog,BlogAdmin)
