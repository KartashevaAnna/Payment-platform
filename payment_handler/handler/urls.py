from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='handler_index'),
    path('personal_page/', views.personal_page, name='personal_page'),
]
