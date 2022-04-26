from django.shortcuts import render
from django.views import generic
from .models import Movie


def index(request):
    return render(request, 'index.html')

def movie_detail(request):
    return render(request, "movie_detail/detail_page.html")


class movieweb(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'movie_detail/movie_list.html'
        movie = Movie.objects.all()
        return render(request, template_name, {"movie":movie})
        