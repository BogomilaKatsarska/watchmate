from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (ReviewList, ReviewDetail, WatchListAV,
                                     WatchDetailAV, StreamPlatformAV,
                                     StreamPlatformDetailAV, ReviewCreate, StreamPlatformVS)

# from watchlist_app.views import movie_list, movie_details
# from watchlist_app.api.views import MovieDetailAV, MovieListAV

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform-details')

urlpatterns = [
    # path('list/', movie_list, name='movie-list'),
    # path('<int:pk>/', movie_details, name='movie-details'),
    # path('list/', MovieListAV.as_view(), name='movie-list'),# CBV need to be utilized with 'as_view'
    # path('<int:pk>/', MovieDetailAV.as_view(), name='movie-details'),
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'), #We comment this URL and the one below becuase of the router
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-details'),
    path('', include(router.urls)),
    # path('review/', ReviewList.as_view(), name='review-detail'),
    # path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-list'), # create a review for specific watch
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
 ]
