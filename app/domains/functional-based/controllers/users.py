# fastapi-opinionated-starter/app/domains/functional-based/controllers/users.py
from fastapi_opinionated.decorators.routing import Get, Post
from fastapi_opinionated_socket.helpers import SocketEvent, socket_api
from fastapi_opinionated.shared.logger import logger
from fastapi_opinionated_eventbus import OnInternalEvent, eventbus_api

@Get("/users-i", group="FUNCTIONALBASED-USERS")
async def list_users():
    users = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
    await eventbus_api().emit("user.retrieved", user_id=1)
    return users

@OnInternalEvent("user.retrieved")
async def handle_user_retrieved_event(user_id: int):
    logger.info(f"User retrieved event handled for user_id: {user_id}")

@Post("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

@Get("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

@Get("/emit_socket_event", group="FUNCTIONALBASED-USERS")
async def emit_socket_event():
    await socket_api().emit("custom_event", {"data": "Hello from FastAPI!"})
    
@SocketEvent("functional_based_event", namespace="/test")
async def functional_based_event_handler(sid, data):
    logger.info(f"Functional-based controller received: {data}")
    
