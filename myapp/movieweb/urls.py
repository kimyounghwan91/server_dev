from django.urls import path, include
from . import views



app_name = "movieweb"

urlpatterns = [  
    path("", views.index.as_view(), name='index'),
    path("movie/1", views.movie_detail, name="movie_detail"),
    path("movie/", views.movieweb.as_view(), name = "movieweb"),
    # path("movie/<int:pk>/", views.deatil_page, name = "detail_page")
]
