from django.shortcuts import render
from .models import Location
from .serializers import LocationSerializer
from rest_framework import generics
import os
from django.http import HttpResponse, Http404
from django.conf import settings

# Create your views here.

def map_view(request):
    locations = Location.objects.all()
    return render(request, 'map.html')

class LocationListCreate(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    
class LocationDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

def download_offline_page(request):
    file_path = os.path.join(settings.BASE_DIR, 'templates', 'offline.html')
    try:
        with open(file_path, 'rb') as file:
          response = HttpResponse(file.read(), content_type='application/octet-stream')
          response['Content-Disposition'] = 'attachment; filename="offline.html"'
          return response
    except FileNotFoundError:
      raise Http404("The offline.html file was not found.")
    
def restaurant_list(request):
    return render(request, 'restaurant.html')

    