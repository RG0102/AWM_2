"""
URL configuration for awmproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import map_view
from rest_framework.routers import DefaultRouter
from .views import LocationListCreate, LocationDetail
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.views.generic import TemplateView
from .views import download_offline_page
from .views import restaurant_list
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', map_view, name='map'),
    path('api/locations/',LocationListCreate.as_view, name='location-list-create'),
    path('api/locations/<int:pk>/', LocationDetail.as_view(), name='location-detail'),
    path('serviceworker.js', include('pwa.urls')),
    path('manifest.json', include('pwa.urls')),
    path('offline/', TemplateView.as_view(template_name="offline.html"), name='offline_page'),
    path('map/', map_view, name='map'),
    path('offline/download/', download_offline_page, name='download-offline-page'),
    path('restaurant/', restaurant_list, name='restaurant_list'),
    path('', RedirectView.as_view(url='/api-v1/restaurants', permanent=True)),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

