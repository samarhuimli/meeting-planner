from django.urls import path
from . import views
#domaine.com/meetings/..

urlpatterns = [
   
    path('', views.meetings_list_view, name='meetings'),  # List of meetings
    path('detail/<int:id>/', views.get_meeting, name='get_meeting'),    

]
