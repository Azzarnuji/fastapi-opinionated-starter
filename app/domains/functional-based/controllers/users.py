from fastapi_opinionated.decorators.routing import Get, Post
from fastapi_opinionated_socket.helpers import SocketEvent, socket_api
from fastapi_opinionated.shared.logger import logger


@Get("/users", group="FUNCTIONALBASED-USERS")
async def list_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@Post("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

@Get("/emit_socket_event", group="FUNCTIONALBASED-USERS")
async def emit_socket_event():
    await socket_api().emit("custom_event", {"data": "Hello from FastAPI!"})
    
@SocketEvent("functional_based_event", namespace="/test")
async def functional_based_event_handler(sid, data):
    logger.info(f"Functional-based controller received: {data}")