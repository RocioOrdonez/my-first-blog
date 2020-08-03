from django.urls import path
from . import views

# Primer patrón a importar
urlpatterns = [
    path('', views.post_list, name='post_list'),
]