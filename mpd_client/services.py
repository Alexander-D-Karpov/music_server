from mpd import MPDClient
from django.conf import settings


class Client:
    def __init__(self):
        self.client = MPDClient()
        self.client.timeout = 20
        self.client.idletimeout = None

    def __enter__(self) -> MPDClient:
        self.client.connect(settings.MPD_HOST, 6600)
        self.client.password(settings.MPD_PASSWORD)
        return self.client

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.disconnect()
