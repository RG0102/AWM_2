import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api-v1/Counties')
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            counties = response.json()  # Parse the JSON response
        else:
            return HttpResponse(f"Error: API returned status code {response.status_code}", status=500)
    
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

    return render(request, 'index.html', {'counties': counties})
import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    try:
        response = requests.get('http://127.0.0.1:8000/api-v1/Counties')

        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            counties = response.json()  # Parse the JSON response
        else:
            return HttpResponse(f"Error: API returned status code {response.status_code}", status=500)
    
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

    return render(request, 'index.html', {'counties': counties})

def restaurant_list(request):
     return render(request, 'restaurant.html')
