import os
from pathlib import Path

import requests
from PIL import Image
from django.conf import settings
from django.core.files import File
from mutagen.id3 import ID3, APIC, TORY, TOPE
from mutagen.mp3 import MP3

from loader.models import Song, Author, Album
from pytube import YouTube, Search
from mutagen.easyid3 import EasyID3
from pydub import AudioSegment

from loader.services.yt_music import search
from random import randint


def download_from_youtube_link(link: str) -> Song:
    yt = YouTube(link)

    if yt.length > 900:
        raise ValueError("Track is too long")

    if not len(yt.streams):
        raise ValueError("There is no such song")

    s = search(yt.title, "albums")
    if s:
        album = s[0]
    else:
        album = None
    thumbnail = None
    if album:
        albm = Album.objects.get_or_create(name=album["title"])[0]
        if "thumbnails" in album:
            thumbnail = album["thumbnails"][-1]["url"]
    else:
        albm = None
    name = yt.title
    author = Author.objects.get_or_create(name=yt.author)[0]
    if Song.objects.filter(name=name, author=author, album=albm).exists():
        return Song.objects.get(name=name, author=author, album=albm)

    audio = yt.streams.filter(only_audio=True).order_by("abr").desc().first()
    orig_path = audio.download(output_path=settings.MEDIA_ROOT)

    # convert to mp3
    path = orig_path.replace(orig_path.split(".")[-1], "mp3")
    AudioSegment.from_file(orig_path).export(path)
    os.remove(orig_path)

    if not thumbnail:
        thumbnail = yt.thumbnail_url

    meta = search(name, "songs")

    author_m = None
    if meta:
        name = meta[0]["title"]
        author_m = [x["name"] for x in meta[0]["artists"]]

    r = requests.get(thumbnail)
    img_pth = str(
        settings.MEDIA_ROOT + f"/{thumbnail.split('/')[-1]}_{str(randint(100, 999))}"
    )
    with open(img_pth, "wb") as f:
        f.write(r.content)

    im = Image.open(img_pth)
    im.save(str(f"{img_pth}.png"))

    os.remove(img_pth)

    tag = MP3(path, ID3=ID3)
    tag.tags.add(
        APIC(
            encoding=3,  # 3 is for utf-8
            mime="image/png",  # image/jpeg or image/png
            type=3,  # 3 is for the cover image
            desc="Cover",
            data=open(str(f"{img_pth}.png"), "rb").read(),
        )
    )
    if albm:
        tag.tags.add(TORY(text=s[0]["year"]))

    if author or author_m:
        if author_m:
            for authr in author_m:
                tag.tags.add(TOPE(text=authr))
        else:
            tag.tags.add(TOPE(text=author.name))

    tag.save()
    os.remove(str(f"{img_pth}.png"))
    tag = EasyID3(path)

    tag["title"] = name
    if albm:
        tag["album"] = albm.name

    tag.save()

    ms_path = Path(path)
    song = Song(name=name, author=author, album=albm)
    with ms_path.open(mode="rb") as f:
        song.file = File(f, name=ms_path.name)
        song.save()
    os.remove(path)
    return song


def search_channel(name):
    s = Search(name)
    vid = s.results[0]  # type: YouTube
    return vid.channel_url
