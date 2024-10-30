
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/',include('website.urls')),#new
    path('meeting/',include('meetings.urls')),
    
]
