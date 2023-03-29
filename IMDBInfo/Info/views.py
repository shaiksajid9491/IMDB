import io
import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .serializers import MovieSerializers
from .models import MovieInfo

try:
    from bs4 import BeautifulSoup
    import requests
    import bs4
    import locale
    import re
except Exception as e:
    print('Caught exception while importing: {}'.format(e))

BASE_URL = "https://www.imdb.com/"
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
response = {}


@api_view(['GET', 'POST'])
def getById(request, slug):
    if request.method == 'GET':
        url = BASE_URL + 'title/' + slug
        print(url)
        source = requests.get(url)
        print(source)
        source.raise_for_status()

        soup = BeautifulSoup(source.content, 'html.parser')
        movie_name = soup.find('h1', attrs={'data-testid': 'hero-title-block__title'}).get_text()
        rating = soup.find('span', class_='sc-7ab21ed2-1 jGRxWM').get_text()
        director = soup.find('a',
                             class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text()
        writers = soup.find('a',
                            class_='ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link').get_text()
        storyline = soup.find('div', class_='ipc-html-content-inner-div').get_text()
        # Storyline section

        # storing results in dictionary
        response['movie_name'] = movie_name
        response['rating'] = rating
        response['director'] = director
        response['writers'] = writers
        response['storyline'] = storyline
        dict_data = response
        print(dict_data)
        print("-----------------------------------------------------")
        # json_data = json.dumps(dict_data)
        record = MovieInfo.objects.create(
            movie_name=dict_data.get('movie_name', None),
            rating=dict_data.get('rating', None),
            director=dict_data.get('director', None),
            writers=dict_data.get('writers', None),
            storyline=dict_data.get('storyline', None)

        )

        serializer_data = MovieSerializers(record).data
        print(serializer_data)
        return Response(serializer_data)

# @api_view(['GET','POST'])
# def createData(request):
#     data = response
#     print(data)
#     if request.method == 'POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=MovieSerializers(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res={'msg':'Data created Successful'}
#             json_data= JSONRenderer().render(res)
#             return HttpResponse(json_data,content='movielist')
#
#         serializer = MovieSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
