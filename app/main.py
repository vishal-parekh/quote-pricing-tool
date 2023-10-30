from fastapi import FastAPI
from app.routers import quote

app = FastAPI()

app.include_router(quote.router)
