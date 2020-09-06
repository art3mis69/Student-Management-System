from django.db import models


from apps.utils.models import Timestamps

class Lecture(Timestamps, models.Model):
    title= models.CharField(max_length=100)
    description = models.TextField()
    lecturer_name = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField()
    slides_url = models.CharField(max_length=100)
    duration = models.IntegerField(range(1,5), help_text = 'Enter number of hours')
    is_required = models.BooleanField(default=True)
