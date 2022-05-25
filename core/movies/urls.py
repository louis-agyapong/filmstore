from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path("list/", views.MovieListAPIView.as_view(), name="list"),
]
