from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from movies.utils import get_movie_data
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from movies.models import Watchlist, Genre, Actor


@login_required(login_url='movies:login')
def home(request):
    return render(request, 'movies/home.html', {'can_add': False})


@login_required(login_url='movies:login')
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
                      

@login_required(login_url = 'movies:login')
def search_watchlist(request):
    q = request.GET['q']
    # distinct method is used cause we get many queryobjects without it
    get_watchlist = Watchlist.objects.filter(Q(title__contains=q)
                                             | Q(genre__movie_genre__contains=q)
                                             | Q(actor__movie_actors__contains=q)).distinct()
    # we can search watched by either 'yes' or 'watched' 
    if q.lower().strip() in ['yes', 'watched']:
        get_watchlist = Watchlist.objects.filter(Q(watched__icontains=1))
    if q.lower().strip() in ['no', 'not watched']:
        get_watchlist = Watchlist.objects.filter(Q(watched__icontains=0))
    return render(request, 'movies/watchlist.html',
                  {'movies_watchlist': get_watchlist})
                      

@login_required(login_url='movies:login')
def watchlist(request):
    movies_watchlist = Watchlist.objects.all()
    context = { 'movies_watchlist': movies_watchlist }
    return render(request, 'movies/watchlist.html', context)


@login_required(login_url='movies:login')
def detail(request, movie_id):
    movie = get_object_or_404(Watchlist, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


@login_required(login_url='movies:login')
def add_item(request):
    title = request.POST['title']
    test = request.POST['actors']
    
    qset = Watchlist.objects.filter(title__contains = title)
    if qset:
        return render(request, 'movies/home.html', {
               'error_message': 'Duplicate found.',
            })
    model = Watchlist(title=request.POST['title'])
    model.save()
    
    for actor in request.POST['actors'].split(', '):
        obj, created = Actor.objects.get_or_create(movie_actors = actor)
        model.actor.add(obj)

    for one_genre in request.POST['genre'].split(', '):
        obj, created = Genre.objects.get_or_create(movie_genre = one_genre)
        model.genre.add(obj)

    return HttpResponseRedirect(reverse('movies:watchlist'))


@login_required(login_url='movies:login')
def delete_item(request, movie_id, template_name='movies/movie_confirm_delete.html'):
    movie = get_object_or_404(Watchlist, pk=movie_id)
    if request.method == 'POST':
        movie.delete()
        return HttpResponseRedirect(reverse('movies:watchlist'))
    return render(request, template_name, {'movie': movie})


@login_required(login_url='movies:login')
def update_item(request, movie_id):
    movie = get_object_or_404(Watchlist, pk=movie_id)
    if request.POST.get('watched'):
        has_watched = True
    else:
        has_watched = False
    movie.watched = has_watched
    movie.save()
    return HttpResponseRedirect(reverse('movies:watchlist'))   

   
def login(request):
    return render(request, 'movies/login.html')

   
def log_out(request):
    return render(request, 'movies/log_out.html') 
