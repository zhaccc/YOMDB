from django.db import models
from django.core.urlresolvers import reverse


class Watchlist(models.Model):
    title = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.TextField()
    actors = models.TextField()
    watched = models.BooleanField(default=False)
    
    class Meta:
        unique_together = ["title", "genre", "actors"]
