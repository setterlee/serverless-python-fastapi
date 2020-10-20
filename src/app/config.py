from starlette.datastructures import CommaSeparatedStrings
import os

class Env:
    def __init__(self):
        #Configuracion Basica
        self.stage = os.getenv("STAGE", "")
        self.version = os.getenv("VERSION", "v1")
        self.project_name = os.getenv("PROJECT_NAME", "Serverless python fastapi")
        self.project_description = os.getenv("PROJECT_DESCRIPTION", "Sample project with python and fastapi")

        #Configuracion Sentry
        self.dsn_sentry = os.getenv("DSN_SENTRY", "")

        #Configuracion Cors
        self.allow_origins = list(CommaSeparatedStrings(os.getenv("ALLOW_ORIGINS", "*")))
        self.allow_credentials = os.getenv("ALLOW_CREDENTIALS", "true").lower() == "true".lower()
        self.allow_methods = list(CommaSeparatedStrings(os.getenv("ALLOW_METHODS", "*")))
        self.allow_headers = list(CommaSeparatedStrings(os.getenv("ALLOW_HEADERS", "*")))


        #Configuracion recursos externos
        self.url_todos = os.getenv("URL_TODOS", "https://jsonplaceholder.typicode.com/todos/1")
env = Env()
