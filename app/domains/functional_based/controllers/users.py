# fastapi-opinionated-starter/app/domains/functional-based/controllers/users.py
from typing import cast
from app.domains.functional_based.middlewares.auth import AuthMiddleware
from app.domains.functional_based.middlewares.hello import hello_world
import fastapi
from fastapi_opinionated.decorators.routing import Get, Post
from fastapi_opinionated.shared.logger import logger
from fastapi_opinionated.middleware.use import UseMiddleware
from app.domains.functional_based.states.auth import AuthState

@Post("/users", group="FUNCTIONALBASED-USERS")
@UseMiddleware(hello_world, AuthMiddleware)
async def create_user(request: fastapi.Request, user: dict):
    try:
        state = AuthState(request)
        return {"id": 1, "user": user, "current_user": state.current_user, "referer": state.referer}
    except Exception as e:
        logger.error(f"Error in create_user: {str(e)}")
        return fastapi.Response(status_code=500, content="Internal Server Error")

@Get("/users", group="FUNCTIONALBASED-USERS")
@UseMiddleware(AuthMiddleware)
async def create_user(request: fastapi.Request):
    try:
        state = AuthState(request)
        return {"id": 3, "user": state.current_user, "referer": state.referer}
    except Exception as e:
        logger.error(f"Error in create_user: {str(e)}")
        return fastapi.Response(status_code=500, content="Internal Server Error")

    
