from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search', views.search, name='search'),
    url(r'^watchlist', views.watchlist, name='watchlist'),
    url(r'^item', views.add_item, name='add_item')
]
