from secrets import choice
import string



ALPHABET: str = string.ascii_letters + string.digits


async def generate_random_slug():
    slug = ""
    for _ in range(6):
        slug += choice(ALPHABET)
    return slug