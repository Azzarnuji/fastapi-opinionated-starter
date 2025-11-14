from fastapi_opinionated.decorators.routing import Controller, Get, Post, Put, Patch, Delete
from fastapi_opinionated_socket.helpers import SocketEvent
from fastapi_opinionated.shared.logger import logger


@Controller("/users", group="CLASSBASED-USERS")
class UsersController:

    @Get("/")
    async def list(self):
        return {"message": "List class-based"}

    @Post("/create")
    async def create(self):
        return {"message": "UsersController created successfully"}

    @Put("/update")
    async def update(self):
        return {"message": "UsersController updated successfully"}
        
    @Patch("/partial_update")
    async def partial_update(self):
        return {"message": "UsersController updated successfully"}

    @Delete("/delete")
    async def delete(self):
        return {"message": "UsersController deleted successfully"}
    
    @staticmethod
    @SocketEvent("class_based_event", namespace="/test")
    async def class_based_event_handler(sid, data):
        logger.info(f"Class-based controller received: {data}")

