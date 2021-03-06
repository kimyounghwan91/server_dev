from django.shortcuts import render
from django.views import generic
from .models import Movie
import random

# def index(request):
#     netflix = Movie.objects.filter(netflix=1) 
#     netflix = {"movie": netflix}
#     return render(request, 'index.html', netflix)


# def movie_detail(request):
#     return render(request, "movie_detail/detail_page.html")


class movieweb(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'movie_detail/movie_list.html'
        movie = Movie.objects.all()
        return render(request, template_name, {"movie":movie})


class index(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        movie = Movie.objects.filter(netflix=1)
        return render(request, template_name, {"movie":movie})


class detailPage(generic.TemplateView):     
    def __init__(self):
        self.template_name  = "movie_detail/detail_page.html" 

    def get_queryset(self):     
        results = Movie.objects.filter(id=self.kwargs['pk'])       
        results = results.values('id', 'title', 'opening_date', 'just_rating', 'imdb_rating', 'runtime', 'synopsis', 'director', 'actors', 'genre','poster_link',)

        return results

    def get(self, request, *args, **kwargs):        
        self.content = {"movieDetail":self.get_queryset()}

        return render(request, self.template_name, self.content)