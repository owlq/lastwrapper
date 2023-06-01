# LastWrapper
LastWrapper is an API wrapper for the [LastFM API](https://last.fm/api).
It is still in early development stages but look forward to more consistant updates

## Installation
Before anything, make sure you have the most up to date pip version.

Windows:
```
py -m pip install --upgrade pip
```
Linux/MAC OS
```
python3 -m pip install --upgrade pip
```

Now we can get into actually installing the package.

Method 1:
```
pip install git+https://github.com/owlq/lastwrapper.git
```
Method 2:
```
python -m pip install -U lastwrapper
```

## Getting an API key
To get an API key, you must first create an account on [LastFM](https://last.fm/join).
Once you have created an account, you can go to the [API page](https://www.last.fm/api/account/create) and create an API key.
Once you have created an API key, you can use it to access the wrapper.

## Examples

This project is mainly used for discord.py, but can be used for other reasons along the way.
Here is an example on how you can use this package in discord.py

```py
import discord, lastwrapper
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(intents=intents, command_prefix='!')

    async def on_ready(self) -> None:
        print(f'Logged in {self.user} | {self.user.id}')

bot = Bot()

@bot.command()
async def lastfm(ctx: commands.Context,  user: str) -> None:
    """Simple command to get the currently playing song, artist, and album of a user"""
    handler = LastFMHandler(username=user, apikey=APIKEY)

    data = await handler.get()
    await ctx.send(f"{user} is currently listening to {data['track']['name']}\n by {data['artist']['name']}\n on {data['album']['name']}")
```
