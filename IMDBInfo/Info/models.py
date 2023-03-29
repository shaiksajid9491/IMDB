from django.db import models


# Create your models here.
class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    director = models.CharField(max_length=50)
    writers = models.CharField(max_length=50)
    storyline = models.TextField()
    slug = models.SlugField(max_length=100)
