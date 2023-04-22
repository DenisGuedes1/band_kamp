from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from songs.pagination import OneItemPage
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView

class SongView(ListCreateAPIView):
     authentication_classes = [JWTAuthentication]
     permission_classes = [IsAuthenticatedOrReadOnly]
     pagination_class = OneItemPage
     queryset = Song.objects.all()
     serializer_class = SongSerializer

     def perform_create(self, serializer):
          album_id = self.kwargs.get('pk')
          album = get_object_or_404(Album, id=album_id)
          serializer.save(album=album)
