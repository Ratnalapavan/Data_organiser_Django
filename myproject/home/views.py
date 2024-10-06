from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is my first Django app!")

def detail(request):
    return HttpResponse("Text Updated to Custome.........")
    # return render(request, 'home/detail.html')
