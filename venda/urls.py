from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('historico', views.historico, name='historico'),
    path('adicionar', views.adicionar, name='adicionar'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
]
