from django.urls import path, include
from rest_framework import routers
from .api.viewsets import BeneficiariosViewSet

router = routers.DefaultRouter()
router.register(r'beneficiarios', BeneficiariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


