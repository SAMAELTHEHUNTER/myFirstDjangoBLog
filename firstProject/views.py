from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request) :
    return render(request , 'about.html')


def Home(request) :
    return render(request , 'Home.html')
