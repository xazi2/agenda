from django.urls import path

from isa_agenda_telefonica.urls import urlpatterns
from . import views

urlpatterns = [

    path('add_contato/', views.add_contato, name='add_contato'),
]