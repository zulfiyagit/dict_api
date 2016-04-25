from rest_framework import serializers
from . import models

class WordsDetailSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Word
		fields = ("id","title","definition","language",'translations', 'synonyms', 'antonyms')

class WordsSerializer(serializers.ModelSerializer):
    class Meta:
    	model = models.Word
    	fields = ('id', 'title', 'definition', 'language')
