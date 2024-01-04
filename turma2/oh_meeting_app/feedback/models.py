from django.db import models
from datetime import datetime
from meeting.models import MyMeeting

class MyFeedback(models.Model):

    myfeedback_id = models.BigAutoField(primary_key=True)
    myfeedback_meeting_id = models.ForeignKey(MyMeeting, on_delete=models.CASCADE,)
    myfeedback_host = models.CharField(max_length=100)
    myfeedback_guest = models.CharField(max_length=100)
    myfeedback_question1 = models.CharField(max_length=300)
    myfeedback_answer1 = models.CharField(max_length=300)
    myfeedback_question2 = models.CharField(max_length=300)
    myfeedback_answer2 = models.CharField(max_length=300)
    myfeedback_question3 = models.CharField(max_length=300)
    myfeedback_answer3 = models.CharField(max_length=300)
    myfeedback_classification = models.IntegerField(default=0)
    myfeedback_cad_hour = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (self.myfeedback_host, self.myfeedback_guest, self.myfeedback_meeting_id.mymeeting_id)