from django.shortcuts import render

""" View to render home page """

def index(request):
    return render(request, 'home/index.html')
