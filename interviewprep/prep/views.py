# views.py
from django.shortcuts import render
from .models import InterviewPrepLink

def interview_preparation(request):
    links = []  # Default empty list

    if request.method == "GET":
        print("this is called")
        technology = request.GET.get('technology')
        experience_level = request.GET.get('experience_level')

        if technology and experience_level:
            links = InterviewPrepLink.objects.filter(technology=technology, experience_level=experience_level)

    return render(request, 'prep/start.html', {'links': links})
def select_technology(request):
    # Your view logic here
    return render(request, 'prep/index.html')

def select_contactform(request):
    return render(request, 'prep/contact.html')