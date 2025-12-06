from fastapi_opinionated.decorators.routing import Get

@Get("/nested")
async def nested_controller():
    return {"message": "This is a nested controller"}