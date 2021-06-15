from os import getenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .database.register import register_tortoise

from .routes.books import router as books_router

app = FastAPI(
    title="Bookhurt API",
    description="API for bookhurt"
)

api = FastAPI(openapi_prefix = "/api")
app.mount("/api", api)
app.mount("/", StaticFiles(directory = "src/static", html = True), name = "html")

api.include_router(books_router, prefix="/books", tags=["Books"])


register_tortoise(app, getenv("DB_URL", "sqlite://:memory:"), True)
