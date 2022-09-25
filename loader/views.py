from django.shortcuts import render

from loader.services.yt import search_channel
from loader.tasks import process_dir, list_tracks


def link(request):
    if request.POST:
        url = request.POST["url"]
        list_tracks.apply_async(kwargs={"url": url})
    return render(request, "video.html")


def dir(request):
    if request.POST:
        path = request.POST["path"]
        process_dir.apply_async(kwargs={"path": path})
    return render(request, "dir.html")


def channel(request):
    if request.POST:
        name = request.POST["name"]
        list_tracks.apply_async(kwargs={"url": search_channel(name)})
    return render(request, "search.html")
