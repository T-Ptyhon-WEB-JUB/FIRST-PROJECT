from django.urls import path
from . import views

tome = "the best"

urlpatterns = [
    path("", views.top_actor, name="my_best_actor"),
]   