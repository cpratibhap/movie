from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
from .models import Movies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ('movie_name', 'actor')

'''
class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = ('movie_name', 'actor')
'''
