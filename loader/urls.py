from django.urls import path

from loader.views import video, channel, playlist, dir

urlpatterns = [
    path("video/", video),
    path("channel/", channel),
    path("playlist/", playlist),
    path("dir/", dir),
]
