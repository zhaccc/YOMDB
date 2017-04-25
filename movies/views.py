from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from movies.utils import get_movie_data
from movies.models import Watchlist


def home(request):
    return render(request, 'movies/home.html', {'can_add': False})


def search(request):
        q = request.GET['q']
        if not q:
            return render(request, 'movies/home.html', {
                'error_message': 'Please input a movie title.',
                'can_add': False
                })

        movie = get_movie_data(q)
        if 'Error' in movie:
            return render(request, 'movies/home.html', {
                'error_message': 'Movie not found.',
                'can_add': False
            })
        return render(request, 'movies/home.html',
                      {'movie': movie, 'query': q, 'can_add': True})


def watchlist(request):
    movies_watchlist = Watchlist.objects.all()
    context = {'movies_watchlist': movies_watchlist}
    return render(request, 'movies/watchlist.html', context)


def add_item(request):
    model = Watchlist(title=request.POST['title'], genre=request.POST['genre'],
                      actors=request.POST['actors'])
    model.save()
    return HttpResponseRedirect(reverse('movies:watchlist'))
    
def delete_item(request, movie_id):
    model = Watchlist.objects.get(id=movie_id)
    model.delete()
    return HttpResponseRedirect(reverse('movies:watchlist'))
