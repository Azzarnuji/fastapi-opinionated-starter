# fastapi-opinionated-starter/app/domains/functional-based/controllers/users.py
from fastapi_opinionated.decorators.routing import Get, Post
from fastapi_opinionated.shared.logger import logger


@Post("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

@Get("/users", group="FUNCTIONALBASED-USERS")
async def create_user(user: dict):
    return {"id": 3, **user}

    
