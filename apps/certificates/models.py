from django.db import models


from apps.utils.models import Timestamps

class Certificate(Timestamps, models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
