from rest_framework import serializers

from albums.models import Album

from .models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'duration','album_id']
   