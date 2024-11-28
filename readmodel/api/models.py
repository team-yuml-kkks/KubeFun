from django.db import models


class SensorReadModel(models.Model):
    timestamp = models.DateTimeField(null=False)
    value = models.IntegerField(null=False)
