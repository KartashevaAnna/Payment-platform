"""payment_handler URL Configuration"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('handler.urls', namespace='handler')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
]
