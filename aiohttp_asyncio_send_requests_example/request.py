import aiohttp  # pip install aiohttp
import asyncio  # o'rnatish shart emas
import pprint   # o'rnatish shart emas


async def main():

    async with aiohttp.ClientSession() as session:
        # so'rov jo'natish kerak bo'lgan manzil
        url = 'https://forbes400.herokuapp.com/api/forbes400'
        async with session.get(url) as resp:
            response = await resp.json()
            # natijani console-ga chiroyli chiqarish uchun
            pprint.pprint(response)

asyncio.run(main())
