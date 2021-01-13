from django.shortcuts import render


def index(request):
    """ to return index page """
    
    return render(request, 'home/index.html')
