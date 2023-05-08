from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns Index page """
    return render(request, 'home/index.html')


def about(request):
    """ Returns about page """
    return render(request, 'home/about.html')
