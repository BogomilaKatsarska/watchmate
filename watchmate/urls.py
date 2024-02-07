from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/dashboard/', admin.site.urls), # change admin/ to something hard to guess/ In this case for test purpose we will use dashboard/
    # path('movie/', include('watchlist_app.urls')),
    path('api/watch/', include('watchlist_app.api.urls')),
    # path('api-auth/', include('rest_framework.urls')), #Temporary LogIn Form
    path('api/account/', include('user_app.api.urls')),
]
