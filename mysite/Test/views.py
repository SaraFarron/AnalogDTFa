from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'Test/homePage.html')

def contact(request):
    return render(request, 'Test/basic.html',
    {'values': ["If you have any questions, please call me",
    "89233692277"]})

def experiments(request):
    return render(request, 'experiments/templates/experiments/experiment.html')
