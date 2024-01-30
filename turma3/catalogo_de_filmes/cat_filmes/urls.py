from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, cadastro, deletar
from rest_framework import routers
from .api.viewsets import FilmeViewSet

router = routers.DefaultRouter()
router.register('api_filmes', FilmeViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('cadastro/', cadastro, name='cadastro'),
    path('deletar/<int:id>', deletar, name='deletar'),
    path('api_filmes/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
