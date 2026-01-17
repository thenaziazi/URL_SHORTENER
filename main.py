from fastapi import FastAPI
from secrets import choice
import string

app = FastAPI()

ALPHABET: str = string.ascii_letters + string.digits


@app.get('/short_url')
async def generate_short_url():
    return {'data': 1}

@app.get('/{slug}')
async def redirect_to_url(slug: str):
    ...


async def generate_random_slug():
    slug = ""
    for _ in range(6):
        choice(ALPHABET) += slug
    return slug
