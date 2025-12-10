from django.contrib import admin

from .models import artist, Album, Song

admin.site.register(artist)
admin.site.register(Album)
admin.site.register(Song)