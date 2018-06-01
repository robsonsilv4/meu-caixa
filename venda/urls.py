from django.urls import path
from . import views


path('historico', views.historico, name='historico'),
