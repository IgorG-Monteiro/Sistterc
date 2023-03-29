from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar, name='iniciar'),
    path('sair', views.sair, name='sair'),
    path('cadastrar', views.cadastrar, name='cadastrar'),
    path('deletar/<int:id>', views.deletar, name='deletar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('gerador', views.gerador, name='gerador'),
    path('gerador_transparencia', views.gerador_transparencia, name='gerador_transparencia'),
    path('base', views.base, name='base'),
    path('start', views.start, name='start'),
]