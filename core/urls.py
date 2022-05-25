from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("core.movies.urls", namespace="movies")),
]
