from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def top_actor(request : HttpRequest):
    my  = "1337"

    return HttpResponse(f"hello world {my}")

