from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from meeting.api.viewsets import MyMeetingViewSet
from feedback.api.viewsets import MyFeedbackViewSet
from pdi.api.viewsets import MyPdiViewSet

router = routers.DefaultRouter()
router.register(r'meeting', MyMeetingViewSet)
router.register(r'feedback', MyFeedbackViewSet)
router.register(r'pdi', MyPdiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
