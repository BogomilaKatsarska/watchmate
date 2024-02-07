from django.urls import path, include
from rest_framework.routers import DefaultRouter
from watchlist_app.api import views
# from watchlist_app.views import movie_list, movie_details
# from watchlist_app.api.views import MovieDetailAV, MovieListAV

router = DefaultRouter()
router.register('stream', views.StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailAV.as_view(), name='movie-details'),
    path('list2/', views.WatchListGV.as_view(), name='watch-details'),
    path('', include(router.urls)),
    path('<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('reviews/', views.UserReview.as_view(), name='user-review-detail'), #/?username=hristo-pc
    #BELOW URLS USED FOR DEMO PURPOSE
    # path('list/', views.movie_list, name='movie-list'),
    # path('<int:pk>/', views.movie_details, name='movie-details'),
    # path('list/', MovieListAV.as_view(), name='movie-list'),# CBV need to be utilized with 'as_view'
    # path('<int:pk>/', MovieDetailAV.as_view(), name='movie-details'),
    # path('stream/', views.StreamPlatformAV.as_view(), name='stream-list'), #We comment this URL and the one below becuase of the router
    # path('stream/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name='stream-details'),
    # path('review/', views.ReviewList.as_view(), name='review-detail'),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    # path('reviews/<str:username>/', views.UserReview.as_view(), name='user-review-detail'),
]