# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('title'))
    genre = models.CharField(max_length=150)
    cover = models.CharField(max_length=300)

    def get_absolute_url(self):
        return reverse('music:detail_album', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=('title'))
    youtube_video_ID = models.CharField(max_length=15)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail_song', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title + ' - ' + self.album.artist
