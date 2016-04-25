from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Word(models.Model):
	title = models.CharField(max_length = 25)
	definition = models.TextField(blank = True)
	language = models.CharField(max_length = 25)
	translaions = models.ManyToManyField('self', blank = True)
	synonyms = models.ManyToManyField('self',blank = True)
	antonyms = models.ManyToManyField('self', blank = True)

	def __str__(self):
		return self.title
