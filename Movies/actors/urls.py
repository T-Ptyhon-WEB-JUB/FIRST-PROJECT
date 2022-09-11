from . import views
from django.urls import path

app_name = 'actors'

urlpatterns = [
    path("topactor/", views.top_actor, name="topactor"), ]
