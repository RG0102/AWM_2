# hotels/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('nearest_hotels/', views.nearest_hotels, name='nearest_hotels'),
]
