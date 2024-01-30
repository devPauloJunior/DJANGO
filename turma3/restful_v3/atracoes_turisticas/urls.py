from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, register
from rest_framework import routers
from .api.viewsets import AtracaoTuristicaViewSet

router = routers.DefaultRouter()
router.register('api_atracoes_turisticas', AtracaoTuristicaViewSet)

urlpatterns = [
    path('index/', index, name='index'),
    path('register/', register, name='register'),
    path('api_atracoes_turisticas/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
