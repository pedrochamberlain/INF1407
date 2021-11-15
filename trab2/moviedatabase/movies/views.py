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

        if form.is_valid():
            movie = form.save(commit=False)
            movie.logged_by = str(request.user)
            movie.save()

            return HttpResponseRedirect(reverse_lazy('movies:list'))
        else:
            return HttpResponseRedirect(reverse_lazy('movies:create'))


class update_movie(View):
    def get(self, request, pk, *args, **kwargs):
        movie = Filme.objects.get(pk=pk)
        form = MovieModelForm(instance=movie)
        context = {'form': form}
        return render(request, 'edit_movie.html', context)

    def post(self, request, pk, *args, **kwargs):
        movie = get_object_or_404(Filme, pk=pk)
        form = MovieModelForm(request.POST, instance=movie)

        if form.is_valid():
            movie = form.save()
            movie.save()
        return HttpResponseRedirect(reverse_lazy('movies:list'))


class delete_movie(View):
    def get(self, request, pk, *args, **kwargs):
        movie = Filme.objects.get(pk=pk)
        movie.delete()

        movies = Filme.objects.all()
        context = {
            'movies': movies
        }

        return HttpResponseRedirect(reverse_lazy('movies:list'))


class list_movies(View):
    def get(self, request, *args, **kwargs):
        movies = Filme.objects.filter(logged_by=request.user)
        context = {
            'movies': movies
        }
        return render(request, 'list_movies.html', context)


class list_all_movies(View):
    def get(self, request, *args, **kwargs):
        movies = Filme.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'list_all_movies.html', context)
