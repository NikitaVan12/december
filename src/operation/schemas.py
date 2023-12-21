from datetime import datetime

from pydantic import BaseModel


class OperationCreate(BaseModel):
    id: int
    quantity: str
    instrument_type: str
    type: str