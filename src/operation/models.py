from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from src.database import metadata

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("instrument_type", String, nullable=True),
    Column("type", String),
)