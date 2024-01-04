from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import MyFeedbackSerializer
from feedback.models import MyFeedback

class MyFeedbackViewSet(viewsets.ModelViewSet):
    queryset= MyFeedback.objects.all()
    serializer_class = MyFeedbackSerializer