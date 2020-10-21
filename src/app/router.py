from fastapi import APIRouter, Header
import src.app.services as services
from typing import List
from src.app.models import InputExample, OutputExample
import src.app.services as services
from starlette.requests import Request

router = APIRouter()

@router.get("/example", tags=["example get"])
async def example_get():
    return await services.example_get()


@router.post("/example", response_model=OutputExample, tags=["example post"])
async def example_endpoint(inputs: InputExample):
    return await services.example_endpoint(inputs)


@router.get("/example-middleware", tags=["example get middleware"])
async def example_middleware():
    return await services.example_middleware()

@router.get("/event", tags=["example get aws event"])
async def get_event(request: Request):
    return {
            "aws_event": request.scope['aws.event']
        }