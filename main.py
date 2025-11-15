
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_opinionated.app import App
from fastapi_opinionated_eventbus.plugin import EventBusPlugin
from fastapi_opinionated_socket.plugin import SocketPlugin
from fastapi.middleware.cors import CORSMiddleware
from fastapi_opinionated_eventbus.plugin import EventBusPlugin

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

App.configurePlugin(
    SocketPlugin(),
    async_mode="asgi",
    cors_allowed_origins=[],
    ping_interval=3,
    ping_timeout=60,
    socketio_path="socket",
)

app = App.create(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)