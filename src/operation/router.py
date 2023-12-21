import time

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import user
from .schemas import OperationCreate
from src.database import get_async_session
from .models import operation


router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@router.get("/")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operation_type)
    result = await session.execute(query)
    return result.all()


@router.post("/add", name='add')
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
        stmt = insert(operation).values(**new_operation.dict())
        await session.execute(stmt)
        await session.commit()
        return {'status':'success'}