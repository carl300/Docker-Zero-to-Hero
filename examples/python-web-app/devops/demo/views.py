from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'demo_site.html')
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django on EC2!")
