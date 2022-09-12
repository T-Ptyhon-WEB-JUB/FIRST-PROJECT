from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# define the views function


def top_actors(request: HttpRequest):
    top_actors_name: str = 'Fatimah'
    return HttpResponse(f'The top actor is {top_actors_name}')


def actor_name(request):
    name = request.GET.get('name') or "Fatimah"
    return HttpResponse('name of the actor is {}'.format(name))
