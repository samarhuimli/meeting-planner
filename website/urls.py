from django.urls import path
from . import views
#domaine.com/website/..

urlpatterns = [
    path('',views.home_view, name='home'),
    path('about',views.about_view, name='about'),
    
]
