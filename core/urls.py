from django.urls import path

from . import views

urlpatterns = [

    path('add_contato/', views.add_contato, name='add_contato'),
    path('editarContato/<int:id>', views.editar_contato, name='editar_contato'),
]