from django.contrib import admin
from .models import Watchlist, Genre, Actor

# Register your models here.
admin.site.register(Watchlist)
admin.site.register(Genre)
admin.site.register(Actor)
