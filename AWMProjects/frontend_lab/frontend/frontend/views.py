from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurant
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, authenticate
from .serializers import RestaurantSerializer
from django.views.decorators.csrf import csrf_exempt #Import csrf_exempt
from django.contrib import messages


# Other views (home, about, contact, etc.)

def home_view(request):
    return render(request, 'home.html')

#Sign up view
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #Save the new user
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        
            if user is not None:
                login(request, user)
                messages.success(request, "Yoy have successfully logged in!")
                return redirect('restaurant_list')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()

    return render(request, 'login.html', {'form': form})
    

def about_view(request):
    return render(request, 'about.html')

def restaurant_list(request):
    #Fetch all restaurant data from database
    restaurants = Restaurant.objects.all()

    #Pass the restaurant data to the template
    return render(request, 'restaurant.html', {'restaurabts': restaurants})
@csrf_exempt
def contact_view(request):
    return render(request, 'contact.html')

def map_view(request, id):
    restaurant = Restaurant.objects.get(id=id)

    #Pss the restaurant data to the template
    return render(request, 'map,html', {'restuarant': restaurant})

    
