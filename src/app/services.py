from asyncio import gather
from src.app.config import env

from fastapi import HTTPException
from src.app.models import InputExample, OutputExample
from src.app.repositories import example

async def example_get():
    """
    Say hej!

    This will greet you properly

    And this path operation will:
    * return "hej!"
    """
    return {"msg": "Hej!"}

async def example_endpoint(inputs: InputExample):
    """
    Multiply two values

    This will multiply two inputs.

    And this path operation will:
    * return a*b
    """
    return {"a": inputs.a, "b": inputs.b, "result": inputs.a * inputs.b}


async def example_middleware():
    """
    Make a request to a external resource
    """

    return await example.get_todos()