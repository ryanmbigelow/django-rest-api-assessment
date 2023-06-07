from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song, Artist

class SongView(ViewSet):

    def retrieve(self, request, pk):
        song = Song.objects.get(pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def list(self, request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
      
    def create(self, request):
        artist = Artist.objects.get(pk=request.data["artist"])
        song = Song.objects.create(
            title=request.data["title"],
            artist_id=artist,
            album=request.data["album"],
            length=request.data["length"],
        )
        serializer = SongSerializer(song)
        return Response(serializer.data)
        
    def update(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.title = request.data["title"]
        artist = Artist.objects.get(pk=request.data["artist"])
        song.artist_id = artist
        song.album = request.data["album"]
        song.time = request.data["time"]
        song.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
      
    def destroy(self, request, pk):
        song = Song.objects.get(pk=pk)
        song.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SongSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Song
        fields = ('id', 'title', 'artist_id', 'album', 'time')
        depth = 1
