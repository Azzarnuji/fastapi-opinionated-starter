from fastapi_opinionated.decorators.routing import Controller, Get, Post, Put, Patch, Delete


@Controller("/users", group="USERS")
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
