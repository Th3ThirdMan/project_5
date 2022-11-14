from django.shortcuts import render

""" View to render index page """

def index(request):
    return render(request, 'home/index.html')
