from django.contrib import admin
from django.urls import path, include
from core.movies import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movies/", include("core.movies.urls", namespace="movies")),
    path("", views.index, name="index"),
]
