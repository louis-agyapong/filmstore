from django.shortcuts import render
from .serializers import MovieSerializer
from rest_framework.generics import ListAPIView
from .models import Movie
from taggit.models import Tag


def index(request):
    movies = Movie.objects.prefetch_related("tags").all()
    tags = Tag.objects.all()
    context = {"movies": movies, "tags": tags}
    return render(request, "core/index.html", context)


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
