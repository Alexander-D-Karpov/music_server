from django.shortcuts import render

# Create your views here.
from pytube import Playlist, Channel

from loader.tasks import process_yb, process_dir


def load_playlist(url: str):
    p = Playlist(url)
    for video in p.video_urls:
        process_yb.apply_async(kwargs={"url": video})


def load_channel(url: str):
    p = Channel(url)
    for video in p.video_urls:
        process_yb.apply_async(kwargs={"url": video})


def video(request):
    if request.POST:
        url = request.POST["url"]
        process_yb.apply_async(kwargs={"url": url})
    return render(request, "video.html")


def channel(request):
    if request.POST:
        url = request.POST["url"]
        load_channel(url)
    return render(request, "channel.html")


def playlist(request):
    if request.POST:
        url = request.POST["url"]
        load_playlist(url)
    return render(request, "playlist.html")


def dir(request):
    if request.POST:
        path = request.POST["path"]
        process_dir.apply_async(kwargs={"path": path})
    return render(request, "dir.html")