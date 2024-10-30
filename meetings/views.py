from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting

# Create your views here.
def meetings_list_view(request):

    meetings = Meeting.objects.all()  # Get all meetings

    return render(request, 'meetings.html', {'meetings': meetings, })

 

def meeting_detail_view(request,id):
    
    meetings = get_object_or_404(Meeting, id=id)
    
    return render (request, 'meetings_Detail.html', {'meetings': meetings})