from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('movie/', include('watchlist_app.urls')),
    path('watch/', include('watchlist_app.api.urls')),
    #Temporary LogIn Form
    path('api-auth/', include('rest_framework.urls'))
]
