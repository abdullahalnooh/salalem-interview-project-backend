import graphene 
from graphene_django import DjangoObjectType 
from .models import artist, Album, Song


class ArtistType(DjangoObjectType): 
    class Meta: model = artist
    fields = ("id", "first_name", "last_name") 

class AlbumType(DjangoObjectType): 
    class Meta: model = Album 
    fields = ("id", "artist", "name", "release_date")

class SongType(DjangoObjectType): 
    class Meta: model = Song 
    fields = ("id", "artist", "album", "title") 


class Query(graphene.ObjectType): 
    all_artists = graphene.List(ArtistType) 
    all_albums = graphene.List(AlbumType) 
    all_songs = graphene.List(SongType) 
    def resolve_all_artists(root, info): return artist.objects.all() 
    def resolve_all_albums(root, info): return Album.objects.all() 
    def resolve_all_songs(root, info): return Song.objects.all() 


schema = graphene.Schema(query=Query)