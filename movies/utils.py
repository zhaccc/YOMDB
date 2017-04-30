import urllib.request
from urllib.request import urlopen
import json


def get_movie_data(title_str):
    # Turns title into URL title.
    title = urllib.parse.quote(title_str)
    request = urlopen("http://www.omdbapi.com/?t={}=&plot=short&type=movie&r=json".format(title))
    response = request.read().decode("utf-8")
    data = json.loads(response)

    movie_data = {}
    if (data['Response'] == 'True'):
        movie_data['Title'] = data['Title']
        movie_data['Actors'] = data['Actors']
        movie_data['Language'] = data['Language']
        movie_data['Rated'] = data['Rated']
        movie_data['Released'] = data['Released']
        movie_data['Plot'] = data['Plot']
        movie_data['Writer'] = data['Writer']
        movie_data['Director'] = data['Director']
        movie_data['Runtime'] = data['Runtime']
        movie_data['Poster'] = data['Poster']
        movie_data['Genre'] = data['Genre']
    else:
        movie_data['Error'] = data['Error']

    return movie_data
