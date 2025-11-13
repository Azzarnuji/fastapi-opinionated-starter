
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_opinionated.app import App


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup code here
        yield
        # Shutdown code here
    except Exception as e:
        print(f"Lifespan error: {e}")

app = App.create(lifespan=lifespan)
