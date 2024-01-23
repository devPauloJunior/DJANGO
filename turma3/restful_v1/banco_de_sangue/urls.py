from django.urls import path, include
from rest_framework import routers
from .api.viewsets import DoadoresViewSet

router = routers.DefaultRouter()
router.register(r'doadores', DoadoresViewSet)

urlpatterns = [
    path('', include(router.urls))
]
