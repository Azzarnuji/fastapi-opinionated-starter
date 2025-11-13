from fastapi_opinionated.decorators.routing import Controller, Get, Post


@Get("/users", group="FUNCTIONALBASED-USERS")
async def list_users():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]

@Post("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}