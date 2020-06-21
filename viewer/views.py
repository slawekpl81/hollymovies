from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# def hello(request, s0):
#     return HttpResponse(f'Hello Django {s0}')
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView

from .models import Movie
from .forms import MovieForm


def start(request):
    return HttpResponse('START: Hello Django')


def hello(request):
    return HttpResponse('Hello Django')


# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all()}
#     )

class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    context_object_name = 'movies'


class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movie_create')
