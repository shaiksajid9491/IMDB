from django.contrib import admin

from .models import MovieInfo


# Register your models here.
# class adminMovieInfo(admin.ModelAdmin):
#     list_display = ['movie_name', 'rating', 'director', 'writters', 'storyline']

admin.site.register(MovieInfo)
# admin.site.register(adminMovieInfo)
