from fastapi_opinionated.decorators.routing import Controller, Get, Post

@Controller("/users")
class UserController:
    
    @Get("/")
    async def list(self):
        return ["john", "budi"]

    @Post("/create")
    async def create(self):
        return {"ok": True}