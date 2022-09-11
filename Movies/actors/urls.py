from django.urls import path
from . import views

# name of app best practise 
app_name = "actors"

# urls pathes 
urlpatterns = [

path('topactors', views.top_actors, name='topactors')

]



