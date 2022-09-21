from pathlib import Path

from django.core.files import File

from loader.models import Song, Author, Album

import mutagen


def load_dir(path: str):
    """should be only run from shell"""
    path = Path(path)

    for f in list(path.glob("**/*.mp3")):
        with f.open("rb") as file:
            s = process_mp3_file(File(file, name=str(f).split("/")[-1]), str(f))
            print(s.name)


def process_mp3_file(file: File, path: str) -> Song:
    tag = mutagen.File(path, easy=True)
    if "artist" in tag:
        author = Author.objects.get_or_create(name=tag["artist"][0])[0]
    else:
        author = None

    if "album" in tag:
        album = Album.objects.get_or_create(name=tag["album"][0])[0]
    else:
        album = None

    song = Song.objects.get_or_create(
        name=tag["title"][0] if "title" in tag else path.split("/")[-1],
        author=author,
        album=album,
    )[0]
    song.file = file
    song.save(update_fields=["file"])

    return song
