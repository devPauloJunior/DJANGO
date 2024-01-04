from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import MyMeetingSerializer
from meeting.models import MyMeeting

class MyMeetingViewSet(viewsets.ModelViewSet):
    queryset= MyMeeting.objects.all()
    serializer_class = MyMeetingSerializer