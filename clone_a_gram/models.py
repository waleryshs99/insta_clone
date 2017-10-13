import datetime

from django.contrib.auth.models import User
from django.db import models


class Photo(models.Model):

    picture = models.ImageField()
    creation = models.DateField(auto_now_add=datetime.datetime.now())
    added_by = models.ForeignKey(User)


class Comment(models.Model):
    body = models.CharField(max_length=256)
    author = models.ForeignKey(User)
    date = models.DateField(auto_now_add=datetime.datetime.now())
    commented_photo = models.ForeignKey(Photo)


class Like(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(User)
