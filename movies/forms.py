from django.forms import Form
from movies.models import Watchlist


class WatchedMovie(Form):
    BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
    watched = forms.ChoiceField(choices=BOOL_CHOICES, widget=forms.RadioSelect())
