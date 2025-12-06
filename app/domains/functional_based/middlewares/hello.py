from fastapi_opinionated.middleware.marker import Middleware
from fastapi_opinionated.middleware.next import Next
from fastapi_opinionated.http.abort import Abort

@Middleware
async def hello_world():
    print("Hello, World Middleware!")
    # if 1 == 1:
    #     Abort(401, "Aborted from HelloWorld Middleware")
    return await Next.run()