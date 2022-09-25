from django.urls import path

from loader.views import link, dir, channel

urlpatterns = [
    path("link/", link),
    path("dir/", dir),
    path("channel/", channel),
]
