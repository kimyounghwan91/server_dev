from django.urls import path, include
from . import views



app_name = "movieweb"

urlpatterns = [  
    path("", views.index),
    path("movie/1", views.movie_detail),
    path("movie/", views.movieweb.as_view(), name = "movieweb")
]