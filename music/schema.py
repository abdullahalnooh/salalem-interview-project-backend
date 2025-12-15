import graphene
from graphene_django import DjangoObjectType
from django.core.exceptions import ObjectDoesNotExist
from graphql import GraphQLError
from .models import Artist, Album, Song

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("id", "first_name", "last_name")


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("id", "artist", "name", "release_date")


class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = ("id", "artist", "album", "title")

class Query(graphene.ObjectType):
    artists = graphene.List(ArtistType)
    albums = graphene.List(AlbumType)
    songs = graphene.List(SongType)

    def resolve_artists(root, info):
        return Artist.objects.all()

    def resolve_albums(root, info):
        return Album.objects.all()

    def resolve_songs(root, info):
        return Song.objects.all()

class CreateArtist(graphene.Mutation):
    artist = graphene.Field(ArtistType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)

    def mutate(self, info, first_name, last_name):
        artist = Artist.objects.create(
            first_name=first_name,
            last_name=last_name
        )
        return CreateArtist(artist=artist)


class UpdateArtist(graphene.Mutation):
    artist = graphene.Field(ArtistType)

    class Arguments:
        id = graphene.ID(required=True)
        first_name = graphene.String()
        last_name = graphene.String()

    def mutate(self, info, id, **kwargs):
        try:
            artist = Artist.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise GraphQLError("Artist not found")

        for k, v in kwargs.items():
            setattr(artist, k, v)
        artist.save()
        return UpdateArtist(artist=artist)


class DeleteArtist(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        deleted, _ = Artist.objects.filter(pk=id).delete()
        if deleted == 0:
            raise GraphQLError("Artist not found")
        return DeleteArtist(ok=True)

class CreateAlbum(graphene.Mutation):
    album = graphene.Field(AlbumType)

    class Arguments:
        artist_id = graphene.ID(required=True)
        name = graphene.String(required=True)
        release_date = graphene.Date(required=True)

    def mutate(self, info, artist_id, name, release_date):
        try:
            artist = Artist.objects.get(pk=artist_id)
        except ObjectDoesNotExist:
            raise GraphQLError("Artist not found")

        album = Album.objects.create(
            artist=artist,
            name=name,
            release_date=release_date
        )
        return CreateAlbum(album=album)


class UpdateAlbum(graphene.Mutation):
    album = graphene.Field(AlbumType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        release_date = graphene.Date()

    def mutate(self, info, id, **kwargs):
        try:
            album = Album.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise GraphQLError("Album not found")

        for k, v in kwargs.items():
            setattr(album, k, v)
        album.save()
        return UpdateAlbum(album=album)


class DeleteAlbum(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        deleted, _ = Album.objects.filter(pk=id).delete()
        if deleted == 0:
            raise GraphQLError("Album not found")
        return DeleteAlbum(ok=True)

class CreateSong(graphene.Mutation):
    song = graphene.Field(SongType)

    class Arguments:
        artist_id = graphene.ID(required=True)
        album_id = graphene.ID(required=True)
        title = graphene.String(required=True)

    def mutate(self, info, artist_id, album_id, title):
        try:
            artist = Artist.objects.get(pk=artist_id)
            album = Album.objects.get(pk=album_id)
        except ObjectDoesNotExist:
            raise GraphQLError("Artist or Album not found")

        song = Song.objects.create(
            artist=artist,
            album=album,
            title=title
        )
        return CreateSong(song=song)


class UpdateSong(graphene.Mutation):
    song = graphene.Field(SongType)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()

    def mutate(self, info, id, **kwargs):
        try:
            song = Song.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise GraphQLError("Song not found")

        for k, v in kwargs.items():
            setattr(song, k, v)
        song.save()
        return UpdateSong(song=song)


class DeleteSong(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(self, info, id):
        deleted, _ = Song.objects.filter(pk=id).delete()
        if deleted == 0:
            raise GraphQLError("Song not found")
        return DeleteSong(ok=True)

class Mutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()
    update_artist = UpdateArtist.Field()
    delete_artist = DeleteArtist.Field()

    create_album = CreateAlbum.Field()
    update_album = UpdateAlbum.Field()
    delete_album = DeleteAlbum.Field()

    create_song = CreateSong.Field()
    update_song = UpdateSong.Field()
    delete_song = DeleteSong.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
