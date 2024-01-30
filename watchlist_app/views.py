# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
#
#
# def movie_list(request):
#     movies = Movie.objects.all() #QuerySelector
#     data = {
#         'movies': list(movies.values())
#     }
#     # print(list(movies.values()))
#
#     return JsonResponse(data)
# '''
# In JSON we:
#     - do not have single quote - only use "double quote"
#     - we write booleans with small letters
# '''
#
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'is_active': movie.is_active,
#     }
#     return JsonResponse(data)
