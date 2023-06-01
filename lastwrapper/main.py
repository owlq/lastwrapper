import aiohttp
from . import http

class LastWrapper(object):
    def __init__(self, username, apikey):
        self.url = 'https://ws.audioscrobbler.com/2.0/'
        self.username = username
        self.session = aiohttp.ClientSession()
        self.apikey = apikey

    async def get(self):
        main = await http.get(self.url, params={
            'method': 'user.getRecentTracks',
            'user': self.username,
            'api_key': self.apikey,
            'format': 'json',
            'limit': 1
        })
        track = main['recenttracks']['track'][0]
        trackinfo = await http.get(self.url, params={
            'method': 'track.getInfo',
            'username': self.username,
            'api_key': self.apikey,
            'artist': track['artist']['#text'],
            'track': track['name'],
            'format': 'json',
            'autocorrect': '1'
        })
        artistinfo = await http.get(self.url, params={
            'method': 'artist.getInfo',
            'username': self.username,
            'api_key': self.apikey,
            'artist': track['artist']['#text'],
            'format': 'json',
            'autocorrect': '1'
        })
        albuminfo = await http.get(self.url, params={
            'method': 'album.getInfo',
            'username': self.username,
            'api_key': self.apikey,
            'artist': track['artist']['#text'],
            'album': track['album']['#text'],
            'format': 'json'
        })

        return {
            'track': {
                'name': trackinfo['track']['name'],
                'url': trackinfo['track']['url'],
                'hyper': f'[{trackinfo["track"]["name"]}]({trackinfo["track"]["url"]})',
                'image': track['image'][3]['#text'],
                'plays': trackinfo['track']['userplaycount'],
            },
            'artist': {
                'name': artistinfo['artist']['name'],
                'url': artistinfo['artist']['url'],
                'hyper': f'[{artistinfo["artist"]["name"]}]({artistinfo["artist"]["url"]})',
                'image': artistinfo['artist']['image'][3]['#text'],
                'plays': artistinfo['artist']['stats']['userplaycount'],
            },
            'album': {
                'name': albuminfo['album']['name'],
                'url': albuminfo['album']['url'],
                'hyper': f'[{albuminfo["album"]["name"]}]({albuminfo["album"]["url"]})',
                'image': albuminfo['album']['image'][3]['#text'],
                'plays': albuminfo['album']['userplaycount'],
            }
        }