from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from movies.services import movie_service

@api_view(['GET'])
def movie_list(request, format=None):
    movies = movie_service.get_movies()
    return Response(movies, status=status.HTTP_200_OK)
