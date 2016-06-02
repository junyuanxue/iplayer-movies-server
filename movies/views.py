from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies import services

@api_view(['GET'])
def movie_list(request, format=None):
    movies = services.get_movie_data()
    print(movies)
    return Response('hello', status=status.HTTP_200_OK)
