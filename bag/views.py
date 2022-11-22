from django.shortcuts import render


def bag_view(request):
    """ A view that shows shopping bag content """

    return render(request, 'bag/bag.html')
