from django.urls import path
from . import views
from .views import restaurant_list

urlpatterns = [
    path('', views.index, name='index'),
    path('restaurants/', restaurant_list, name='restaurant_list')
]
