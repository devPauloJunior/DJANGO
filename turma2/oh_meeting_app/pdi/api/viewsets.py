from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import MyPdiSerializer
from pdi.models import MyPdi

class MyPdiViewSet(viewsets.ModelViewSet):
    queryset= MyPdi.objects.all()
    serializer_class = MyPdiSerializer