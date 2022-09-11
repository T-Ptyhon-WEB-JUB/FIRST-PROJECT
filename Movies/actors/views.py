from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def top_actor(request):
    # return an image as a response
    return HttpResponse('<img src="https://m.media-amazon.com/images/M/MV5BMTQzMzg1ODAyNl5BMl5BanBnXkFtZTYwMjAxODQ1._V1_UX178_CR0,0,178,264_AL_.jpg"></img>')
