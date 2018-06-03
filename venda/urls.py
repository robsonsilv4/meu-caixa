from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('historico', views.historico, name='historico'),
]
