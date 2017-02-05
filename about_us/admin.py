from django.contrib import admin

# Register your models here.
from about_us.models import Rate, Resident

admin.site.register(Rate)


class ResidentAdmin(admin.ModelAdmin):
    list_display = 'name position'.split()


admin.site.register(Resident,ResidentAdmin)
