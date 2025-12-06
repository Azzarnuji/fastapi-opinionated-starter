import fastapi
from fastapi_opinionated.middleware import Middleware
from fastapi_opinionated.middleware import Next
from typing import cast
from app.domains.functional_based.states.auth import AuthState
def get_current_user():
    # Dummy implementation for current user retrieval
    return {"username": "test_user"}

@Middleware
async def AuthMiddleware(
    request: fastapi.Request,
    current_user = fastapi.Depends(get_current_user),
):
    headers = request.headers
    referer = headers.get("Referer", "")
    AuthState(request, current_user=current_user, referer=referer)
    print(f"Auth Middleware: Current User - {current_user}, Referer - {referer}")
    return await Next.run()