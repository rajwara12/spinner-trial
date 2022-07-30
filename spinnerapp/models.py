
from time import time
from django.db import models
from datetime import datetime 


# Create your models here.


class Wheel(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)
    starting_point = models.IntegerField(default=0, null=False)
    ending_point = models.IntegerField(default=0, null=False)
    desc = models.TextField()
    img = models.ImageField(null=True,upload_to = 'images',default='intro.png')

    def __str__(self):
        return self.name

class History(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name + ' --------- ' + str(self.timestamp)