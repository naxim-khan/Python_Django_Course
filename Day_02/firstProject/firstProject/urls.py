from django.contrib import admin
from django.urls import path, include
from challenges.views import index  # Import the index view from challenges app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Add a default view for the root URL
    path('challenges/', include('challenges.urls')),  # Remove trailing slash here
]
