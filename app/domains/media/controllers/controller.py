from fastapi_opinionated.decorators.routing import Controller, Get, Post, Put, Patch, Delete


@Controller("/media", group="MEDIA")
class MediaController:

    @Get("/")
    async def list(self):
        return {"message": "List media"}

    @Post("/create")
    async def create(self):
        return {"message": "MediaController created successfully"}

    @Put("/update")
    async def update(self):
        return {"message": "MediaController updated successfully"}
        
    @Patch("/partial_update")
    async def partial_update(self):
        return {"message": "MediaController updated successfully"}

    @Delete("/delete")
    async def delete(self):
        return {"message": "MediaController deleted successfully"}
