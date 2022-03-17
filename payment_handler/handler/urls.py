from django.urls import path
from . import views

app_name = 'handler'

urlpatterns = [
    path('', views.index, name='handler_index'),
    path('handler/', views.personal_page, name='personal_page'),
]
