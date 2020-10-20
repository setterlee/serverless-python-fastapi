import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from mangum import Mangum
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.app.config import env
from src.app.router import router

app = FastAPI(
    title=env.project_name,
    description=env.project_description,
    version=env.version,
    openapi_prefix=f'/{env.stage}' if env.stage != '' else '/'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=env.allow_origins,
    allow_credentials=env.allow_credentials,
    allow_methods=env.allow_methods,
    allow_headers=env.allow_headers,
)


if env.dsn_sentry != '':
    sentry_sdk.init(
        dsn=env.dsn_sentry,
        environment=env.stage)
    app.add_middleware(SentryAsgiMiddleware)


@app.exception_handler(Exception)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=500, content={
        exc.__class__.__name__: str(exc)
    }, headers={
        'access-control-allow-credentials': 'true',
        'access-control-allow-origin': '*'
    })

app.include_router(router)

handler = Mangum(app, enable_lifespan=False)