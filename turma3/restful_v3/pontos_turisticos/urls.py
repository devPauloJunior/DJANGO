from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index, register

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
