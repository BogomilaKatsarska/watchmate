from django.urls import path, include

import watchlist_app
from watchlist_app.views import movie_list

urlpatterns = [
    path('list/', movie_list, name='movie-list'),
]
