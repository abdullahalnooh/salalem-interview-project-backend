from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    def __str__(self):
        return f"{self.artist} {self.name} {self.release_date}"

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.artist} {self.album} {self.title}"
