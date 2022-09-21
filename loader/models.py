import uuid as uuid
from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Song(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="")
    author = models.ForeignKey(
        Author, null=True, related_name="songs", on_delete=models.SET_NULL
    )
    album = models.ForeignKey(
        Album, null=True, related_name="songs", on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
