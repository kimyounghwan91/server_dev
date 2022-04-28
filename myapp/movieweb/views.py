from django.shortcuts import render
from django.views import generic
from .models import Movie
import random

def index(request):
    netflix = Movie.objects.filter(netflix=1) 
    netflix = {"movie": movie}
    return render(request, 'index.html', netflix)


def movie_detail(request):
    return render(request, "movie_detail/detail_page.html")


class movieweb(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'movie_detail/movie_list.html'
        movie = Movie.objects.all()
        return render(request, template_name, {"movie":movie})


