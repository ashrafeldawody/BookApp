from django.http import HttpResponse
from django.shortcuts import render

from auther.models import Auther

def get_all(request):
    authers = Auther.objects.all()
    return render(request, 'auther/index.html', {"authers": authers})

def get_by_id(request, auther_id):
    auther = Auther.objects.get(id=auther_id)
    return render(request, 'auther/show.html', {"auther": auther})
