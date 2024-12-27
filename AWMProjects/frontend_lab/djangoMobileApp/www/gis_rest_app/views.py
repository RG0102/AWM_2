from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurant
from .serializers import RestaurantSerializer

class RestaurantListView(APIView):
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()  # Query all the restaurant objects
        serializer = RestaurantSerializer(restaurants, many=True)  # Serialize the queryset
        return Response({"restaurants": serializer.data})  # Return the data as JSON
