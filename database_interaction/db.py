import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

load_dotenv()
pwd = os.getenv('POSTGRES_PASSWORD')


engine = create_async_engine(
    url= f"postgresql+asyncpg://postgres:{pwd}@localhost:5432/avito_tz"
)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)