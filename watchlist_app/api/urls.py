from django.urls import path, include

from watchlist_app.api.views import (ReviewList, ReviewDetail, WatchListAV,
                                     WatchDetailAV, StreamPlatformAV,
                                     StreamPlatformDetailAV)

# from watchlist_app.views import movie_list, movie_details
# from watchlist_app.api.views import MovieDetailAV, MovieListAV

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),
    # path('list/', MovieListAV.as_view(), name='movie-list'),# CBV need to be utilized with 'as_view'
    # path('<int:pk>/', MovieDetailAV.as_view(), name='movie-details'),
    path('list/', WatchListAV.as_view(), name='watch-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='watch-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-details'),

    path('review/', ReviewList.as_view(), name='review-detail'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

#     path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
#     path('stream/review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
 ]
