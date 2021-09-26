from django.contrib import admin
from first.models import GeoHistory

# Register your models here.
class GeoAdmin(admin.ModelAdmin):
    list_display = ('author', 'date')


admin.site.register(GeoHistory, GeoAdmin)