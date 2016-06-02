from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def movie_list(request, format=None):
    return Response('hello', status=status.HTTP_200_OK)
