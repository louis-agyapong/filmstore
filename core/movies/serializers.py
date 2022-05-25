from rest_framework import serializers
from taggit.serializers import TaggitSerializer, TagListSerializerField

from .models import Movie


class MovieSerializer(TaggitSerializer ,serializers.ModelSerializer):
    tags = TagListSerializerField()
    class Meta:
        model = Movie
        fields = ("id", "name", "director", "description", "year", "tags")
