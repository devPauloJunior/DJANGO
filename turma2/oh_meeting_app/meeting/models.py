from django.db import models
from datetime import datetime

class MyMeeting(models.Model):
    STATUS_CHOICES =  [
        ('AB', 'Aberta'),
        ('EN', 'Encerrada')
    ]

    PLACE_CHOICES = [
        ('PRE', 'Presencial'),
        ('ONL', 'On-line')
    ]

    mymeeting_id = models.BigAutoField(primary_key=True)
    mymeeting_host = models.CharField(max_length=100)
    mymeeting_guest = models.CharField(max_length=100)
    mymeeting_title = models.CharField(max_length=100)
    mymeeting_desc = models.CharField(max_length=300)
    mymeeting_place = models.CharField(max_length=3, choices=PLACE_CHOICES)
    mymeeting_link = models.URLField(max_length=300, blank=True)
    mymeeting_room = models.CharField(max_length=100, blank=True)
    mymeeting_status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    mymeeting_date = models.DateField(blank=True)
    mymeeting_hour = models.TimeField(blank=True)
    mymeeting_cad_hour = models.DateTimeField(default=datetime.now, blank=True)

    def __str__ (self):
        return str(self.mymeeting_id)