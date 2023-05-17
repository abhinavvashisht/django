from django.shortcuts import render
from .models import Announcements

# Create your views here.

announcements = Announcements.objects.all()


context = {
    'announcements': announcements
}

def home(request):
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')