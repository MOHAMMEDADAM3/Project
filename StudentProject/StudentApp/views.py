from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello world!")
def website(request):
    return render(request,'website.html')
def dashboard(request):
    return render(request,'dashboard.html')
def attendance(request):
    return render(request,'attendance.html')


# Create your views here.
