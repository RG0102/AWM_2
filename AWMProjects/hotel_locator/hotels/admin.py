# hotels/admin.py
from django.contrib import admin
from .models import Hotel

# Register the Hotel model to make it available in the admin interface
admin.site.register(Hotel)

