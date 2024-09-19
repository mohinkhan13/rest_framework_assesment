from django.shortcuts import render
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

class snippet_list(generics.ListCreateAPIView):
	queryset=Snippet.objects.all()
	serializer_class=SnippetSerializer

class snippet_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Snippet
    serializer_class=SnippetSerializer
