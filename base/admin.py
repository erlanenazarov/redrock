from django.contrib import admin

# Register your models here.
from base.models import Category, Tour, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name image'.split()

    def image(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.icon.url
        except:
            return '<p>No Cover</p>'

    image.allow_tags = True


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class TourAdmin(admin.ModelAdmin):
    list_display = 'title icon category'.split()
    exclude = 'down'.split()
    readonly_fields = 'created_at updated_at'.split()

    def icon(self, obj):
        try:
            return '<img src="%s" style = "width:50px; height=50px;" />' % obj.image.url
        except:
            return '<p>No Cover</p>'

    icon.allow_tags = True

    inlines = [CommentInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tour, TourAdmin)
