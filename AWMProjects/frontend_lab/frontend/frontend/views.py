from django.shortcuts import render

def restaurant_list(request):
    return render(request, 'restaurant.html')
