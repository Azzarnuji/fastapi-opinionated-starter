
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_opinionated.app import App
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup code here
        print("App is completed initialization.")
        yield
        print("App is shutting down...")
        # Shutdown code here
    except Exception as e:
        print(f"Lifespan error: {e}")

app = App.create(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)