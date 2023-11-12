from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.PROTECT,
        primary_key=True
    )
    lon = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return str(self.lon), str(self.lat)
