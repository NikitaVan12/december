from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.operation.models import operation
from src.operation.schemas import OperationCreate
from src.operation.router import get_specific_operations

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory='src/templates')


@router.get("/base", name='base')
def get_base_page(request: Request):
    return templates.TemplateResponse("lobby.html", {"request": request})


@router.get("/search/{operation_type}", name='search')
def get_search_page(request: Request, operations=Depends(get_specific_operations)):
    return templates.TemplateResponse("search.html", {"request": request, "operations": operations})

@router.get('/add')
def get_specific_operations(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})