# admin.py
from django.contrib import admin
from .models import Location  # Import Location from models.py

# Register the Location model with the admin site
admin.site.register(Location)
