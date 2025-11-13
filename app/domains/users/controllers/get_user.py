from fastapi_opinionated.decorators.routing import Controller, Get, Post


@Controller("/get_user", group="GET_USER")
class GetUserController:
    
    @Get("/{user_id}")
    def get_user(self, user_id: int):
        return {"user_id": user_id, "name": "John Doe"}
