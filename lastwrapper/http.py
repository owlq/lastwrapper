import orjson
import aiohttp
from typing import Optional

async def get(url: str, headers: Optional[dict] = None, params: Optional[dict] = None,) -> dict:
    """Make an asynchronous HTTP request to the specified URL and return the JSON response as a dictionary."""
    data = await grab(url, headers, params)
    return orjson.loads(data) if data else {}

async def grab(url: str, headers: Optional[dict] = None, params: Optional[dict] = None,) -> bytes:
    """Make an asynchronous HTTP request to the specified URL and return the raw response data."""
    total_size = 0
    data = b''

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url, params=params) as response:
            while True:
                chunk = await response.content.read(4*1024)
                data += chunk
                total_size += len(chunk)

                if not chunk:
                    break

                if total_size > 500_000_000:
                    return None

    return data