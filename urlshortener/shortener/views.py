from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from .models import URL
from .serializers import URLSerializer
    
# Create your views here.

class URLShortenView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer


class URLRedirectView(generics.RetrieveAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'short_url'
