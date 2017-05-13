from django.db import models
from django.core.urlresolvers import reverse


class Genre(models.Model):
    movie_genre = models.TextField()
    
    def __str__(self):
        return '{}'.format(self.movie_genre)
    

class Actor(models.Model):
    movie_actors = models.TextField()


class Watchlist(models.Model):
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)   
    watched = models.BooleanField(default=False)
    
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
