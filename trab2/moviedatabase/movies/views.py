from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import View

from movies.models import Filme
from movies.forms import MovieModelForm


class create_movie(View):
    def get(self, request, *args, **kwargs):
        context = {'form': MovieModelForm}
        return render(request, 'add_movie.html', context)

    def post(self, request, *args, **kwargs):

        form = MovieModelForm(request.POST)
        if(form.is_valid()):
            movie = form.save()
            movie.save()

            return HttpResponseRedirect(reverse_lazy('list_movies'))
        else:
            return HttpResponseRedirect(reverse_lazy('add_movie'))


class update_movie(View):
    def get(self, request, pk, *args, **kwargs):
        movie = Filme.objects.get(pk=pk)
        form = MovieModelForm(instance=movie)
        context = {'form': form}
        return render(request, 'update_movie.html', context)

    def post(self, request, pk, *args, **kwargs):
        movie = get_object_or_404(Filme, pk=pk)
        form = MovieModelForm(request.POST, instance=movie)

        if(form.is_valid()):
            movie = form.save()
            movie.save()
        return HttpResponseRedirect(reverse_lazy('list_movies'))


class list_movies(View):
    def get(self, request, *args, **kwargs):
        movies = Filme.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'list_movies.html', context)
