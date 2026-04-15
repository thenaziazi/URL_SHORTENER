from fastapi import FastAPI, Body
from contextlib import asynccontextmanager
from database_interaction.db import engine
from database_interaction.models import Base
from service import generate_short_url


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield
    ...

app = FastAPI(lifespan=lifespan)



@app.post('/short_url')
async def generate_slug(
    long_url: str = Body(embed=True),
):
    new_slug = await generate_short_url(long_url=long_url)
    return {'data': new_slug}



@app.get('/{slug}')
async def redirect_to_url(slug: str):
    ...
