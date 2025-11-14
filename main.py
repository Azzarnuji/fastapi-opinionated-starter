
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_opinionated.app import App
from fastapi_opinionated_socket.plugin import SocketPlugin
from fastapi.middleware.cors import CORSMiddleware
import socketio

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup code here
        yield
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
App.enable(
    SocketPlugin(),
    async_mode="asgi",
    cors_allowed_origins=[],
    ping_interval=3,
    ping_timeout=60,
    socketio_path="socket",
)