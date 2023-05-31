from django.shortcuts import render
from app.models import *
# Create your views here.

def topic_data(request):
    dt=Topic.objects.all()
    d={'dt':dt}
    return render(request,'fulldata.html',d)

def webpage_data(request):
    dt=Webpage.object.all()
    d={'dt':dt}
    return render(request,webpage_data,d)

def detail_data(request):
    dt=Detail.objects.all()
    d={'dt':dt}
    return render(request,'detail_data.html',d)