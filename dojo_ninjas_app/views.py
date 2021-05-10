from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos': Dojo.objects.all(),
    }
    return render(request, 'index.html', context)


def dojo(request):
    name = request.POST['name']
    city = request.POST['city']
    state= request.POST['state']

    Dojo.objects.create(name=name, city=city, state=state)
    
    return redirect('/')

def ninja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id = request.POST['dojo']
    )

    return redirect('/')
