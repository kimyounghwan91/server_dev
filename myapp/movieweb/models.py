from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=4000, blank=True, null=True)
    opening_date = models.CharField(max_length=1000, blank=True, null=True)
    just_rating = models.CharField(max_length=1000, blank=True, null=True)
    imdb_rating = models.CharField(max_length=1000, blank=True, null=True)
    runtime = models.CharField(max_length=500, blank=True, null=True)
    synopsis = models.CharField(max_length=4000, blank=True, null=True)
    director = models.CharField(max_length=1000, blank=True, null=True)
    actors = models.CharField(max_length=4000, blank=True, null=True)
    genre = models.CharField(max_length=4000, blank=True, null=True)
    poster_link = models.CharField(max_length=1000, blank=True, null=True)
    netflix = models.IntegerField(blank=True, null=True)
    disneyplus = models.IntegerField(blank=True, null=True)
    wavve = models.IntegerField(blank=True, null=True)
    watcha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movie'
        ordering = ['-opening_date']