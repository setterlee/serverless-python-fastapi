from src.app.config import env
import src.app.repositories.utils as utils
import json


async def get_todos():

    url = env.url_todos
    
    headers = {
    }

    response = await utils.get(url=url, headers=headers)

    return response
