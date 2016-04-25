from django.shortcuts import render
from rest_framework import viewsets
from . import forms
from . import models
from rest_framework import generics
from rest_framework import filters
# Create your views here.

class WordsViewSet(generics.ListAPIView):
    serializer_class = forms.WordsSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        language = self.kwargs['language']
        return models.Word.objects.filter(language=language).order_by('title')

class DetailViewSet(generics.ListAPIView):
    serializer_class = forms.WordsDetailSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        language = self.kwargs['language']
        identifier = self.kwargs['id']
        return models.Word.objects.filter(language=language,id=identifier).order_by('title')



