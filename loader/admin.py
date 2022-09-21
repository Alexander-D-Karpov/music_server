from django.contrib import admin

# Register your models here.
from loader.models import Song, Author, Album

admin.site.register(Song)
admin.site.register(Author)
admin.site.register(Album)
