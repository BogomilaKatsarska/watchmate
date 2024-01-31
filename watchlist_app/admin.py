from django.contrib import admin
from watchlist_app.models import StreamPlatform, WatchList, Review


# from watchlist_app.models import Movie


@admin.register(StreamPlatform)
class StreamPlatformAdmin(admin.ModelAdmin):
    pass


@admin.register(WatchList)
class WatchListAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
# @admin.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     pass
