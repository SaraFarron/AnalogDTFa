from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'basic/homePage.html')

def contact(request):
    return render(request, 'basic/basic.html',
    {'values': ["If you have any questions, please call me",
    "89233692277"]})

def experiments(request):
    return render(request, 'experiments/experiment.html')