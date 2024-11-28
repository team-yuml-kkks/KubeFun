from django.contrib import admin

from .models import SensorReadModel


class SensorReadModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(SensorReadModel, SensorReadModelAdmin)
