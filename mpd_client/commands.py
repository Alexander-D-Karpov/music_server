from rest_framework.exceptions import NotFound

from loader.models import Song
from mpd_client.services import Client


def get_song() -> dict:
    with Client() as client:
        data = client.currentsong()

    print(data)

    qs = Song.objects.filter(
        file=data["file"], author__name=data["artist"] if "artist" in data else None
    )

    print(qs)

    if qs.exists():
        return qs.first()
    raise NotFound


def next():
    with Client() as client:
        client.next()
    return


def shuffle():
    with Client() as client:
        client.shuffle()
    return


def pause():
    with Client() as client:
        client.pause()
    return


def previous():
    with Client() as client:
        client.previous()
    return


def set_random():
    with Client() as client:
        client.random(1)
    return


def unset_random():
    with Client() as client:
        client.random(0)
    return


def status() -> dict:
    with Client() as client:
        data = client.status()
        stats = client.stats()
    data.update(stats)
    return data


def play(song: Song):
    with Client() as client:
        res = client.playlistsearch(song.name)
    print(res)
