from aiohttp import request

async def post(url, headers, data=None, json=None):
    async with request('POST',url=url,
                            headers=headers,
                            json=json, data=data) as response:
        
        if (response.status >= 300):
            raise Exception('Error ejecutando post: ' + await response.text())
        return await response.json()

async def get(url, headers=None):
    async with request('GET',url=url,
                            headers=headers) as response:
        if (response.status >= 300):
            raise Exception('Error ejecutando post: ' + await response.text())
        return await response.json()
        