from fastapi_opinionated.app import App
from fastapi_opinionated.decorators.routing import Controller, Get, Post
from socketio import AsyncServer
from fastapi_opinionated_socket.helpers import socket_api


@Get("/users", group="FUNCTIONALBASED-USERS")
async def list_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@Post("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

@Get("/emit_socket_event", group="FUNCTIONALBASED-USERS")
async def emit_socket_event():
    await socket_api().emit("custom_event", {"data": "Hello from FastAPI!"})