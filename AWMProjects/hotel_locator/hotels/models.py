# hotels/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name
