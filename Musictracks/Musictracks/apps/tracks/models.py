from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Genre(models.Model):
	genre_name = models.CharField(max_length=20)

	class Meta:
		db_table = 'genre'
		verbose_name='genre'
        verbose_name_plural = 'genres'

	def __unicode__(self):
		return '%s' % self.genre_name

class Track(models.Model):
	title = models.CharField(max_length=50)
	genre = models.ForeignKey(Genre,related_name='genre')
	rating = models.IntegerField(default=4)

	class Meta:
		db_table = 'track'
		verbose_name='track'
        verbose_name_plural = 'tracks'


	def __unicode__(self):
		return '%s' % self.title 