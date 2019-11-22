from .serializers import MoviesSerializer
from rest_framework import generics
# from rest_framework.viewsets import ModelViewSet
from .models import Movies

# Create your views here.


class GetMoviesView(generics.ListAPIView):
    queryset = Movies.objects.all()     # To get the objects from the database
    serializer_class = MoviesSerializer   # In serializing and de-serializing the data


'''
class GetMoviesView(ModelViewSet):
    queryset = Movies.objects.all()     # To get the objects from the database
    serializer_class = MoviesSerializer   # In serializing and de-serializing the data
'''

