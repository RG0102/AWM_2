# In gis_rest_app/urls.py (or your relevant app's URL configuration)
from django.urls import path
from .views import RestaurantListView
from django.shortcuts import redirect

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurants'),
    # Ensure this is the correct view
    # or path('Counties', views.counties, name='counties') if it's a function-based view
]
