from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search$', views.search, name='search'),
    url(r'^querywatchlist', views.search_watchlist, name='search_watchlist'),
    url(r'^watchlist', views.watchlist, name='watchlist'),
    url(r'^item$', views.add_item, name='add_item'),
    url(r'^delete/(?P<movie_id>\d+)$', views.delete_item, name='delete_item'),
    url(r'^update/(?P<movie_id>\d+)$', views.update_item, name='update_item'),
    url(r'^detail/(?P<movie_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^login/$', auth_views.login, {'template_name': 'movies/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'movies/log_out.html'}, name='logout')
]
