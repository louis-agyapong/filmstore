from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework.generics import ListAPIView
from .models import Movie


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
