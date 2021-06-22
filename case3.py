import aiohttp
import asyncio
import json
from pprint import pprint


async def get(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.content.read()


async def main():
    users = await get('https://jsonplaceholder.typicode.com/users')
    posts = await get('https://jsonplaceholder.typicode.com/posts')
    comments = await get('https://jsonplaceholder.typicode.com/comments')

    pprint(json.loads(users))
    pprint(json.loads(posts))
    pprint(json.loads(comments))


if __name__ == '__main__':
    asyncio.run(main())


# Как ускорить получение данных?
