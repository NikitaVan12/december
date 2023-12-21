from fastapi_users import FastAPIUsers

from fastapi import FastAPI
from starlette.templating import Jinja2Templates

from .operation.router import router as router_operation
from .auth.base_config import auth_backend
from .database import User
from .auth.manager import get_user_manager
from .auth.schemas import UserRead, UserCreate
from .page.router import router as router_page


templates = Jinja2Templates(directory='src/templates')

app = FastAPI(
    title="shop"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)



app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


app.include_router(router_operation)
app.include_router(router_page)