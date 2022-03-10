from django.shortcuts import render
from watchlist_app.models import Movie

def movie_list(request):
  movies = Movie.objects.all()
  
  
