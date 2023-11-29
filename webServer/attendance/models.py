from django.db import models
import datetime

# Create your models here.

class Students(models.Model):
    card_id = models.IntegerField()
    name = models.CharField(max_length=30, default="myName")
    team = models.CharField(max_length=30, default="AUV")

    def __str__(self):
        return str(self.name) + ' : ' + str(self.card_id)
        

class Logs(models.Model):
    card_id = models.IntegerField()
    name = models.CharField(max_length=30)
    team = models.CharField(max_length=30)
    date = models.DateField(default=datetime.datetime.now())
    time_in = models.TimeField(default=datetime.datetime.now())
    time_out = models.TimeField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + ' : ' + str(self.date)