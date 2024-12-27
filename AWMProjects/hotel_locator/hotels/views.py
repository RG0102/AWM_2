from django.http import JsonResponse
from .models import Hotel
from math import radians, sin, cos, sqrt, atan2

# Haversine formula to calculate distance between two geographical coordinates
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c  # Distance in kilometers
    return distance

def nearest_hotels(request):
    # Get the user's latitude and longitude from query parameters
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')

    # Check if the latitude and longitude are provided
    if not latitude or not longitude:
        return JsonResponse({'error': 'Latitude and Longitude are required'}, status=400)

    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        return JsonResponse({'error': 'Invalid latitude or longitude'}, status=400)

    # Query all hotels from the database
    hotels = Hotel.objects.all()
    nearest_hotels = []

    # Calculate the distance to each hotel and filter by proximity
    for hotel in hotels:
        distance = haversine(latitude, longitude, hotel.latitude, hotel.longitude)
        nearest_hotels.append({
            'name': hotel.name,
            'latitude': hotel.latitude,
            'longitude': hotel.longitude,
            'distance': distance  # Distance to the user in km
        })

    # Sort hotels by distance
    nearest_hotels = sorted(nearest_hotels, key=lambda x: x['distance'])

    # Return the list of nearest hotels
    return JsonResponse(nearest_hotels, safe=False)
