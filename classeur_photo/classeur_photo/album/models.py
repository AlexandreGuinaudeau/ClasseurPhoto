from __future__ import unicode_literals

from django.db import models
from utils import pretty_print


class Album(models.Model):
    """
    name: Name of the album (ex: Vietnam 2016)
    permalink: url of the album (ex: vietnam_2016)
    path: Absolute path to the root folder containing the photos of the album (local folder or url)
    """
    name = models.CharField(max_length=200)
    permalink = models.CharField(max_length=200, unique=True)
    path = models.CharField(max_length=200)

    def __str__(self):
        return pretty_print(self, ['id', 'name', 'path'])


class Photo(models.Model):
    """
    album: Album this photo is part of (ex: Vietnam)
    cluster_name: Cluster of photos this photo is part of (ex: Night Market in Da Lat). Defaults to album.name
    photo_name: Name of the photo. Defaults to 'cluster_name num_in_cluster"
    date: Date the photo was taken
    photo_path: Relative path to the photo, within the album
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date = models.DateTimeField()
    path = models.CharField(max_length=200)
    cluster_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return pretty_print(self, ['id', 'album_id', 'date', 'path', 'cluster_name', 'name'])
