from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('checkouts.urls')),
    path('valida', include('valida.urls')),
]
