from celery import shared_task

from loader.services.file import load_dir
from loader.services.yt import download_from_youtube_link


@shared_task
def process_yb(url):
    download_from_youtube_link(url)
    return url


@shared_task
def process_dir(path):
    load_dir(path)
    return path
