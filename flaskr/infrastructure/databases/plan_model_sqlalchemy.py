from sqlalchemy import Column, String, Numeric, DateTime
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
import uuid

Base = declarative_base()

class PlanModelSqlAlchemy(Base):
    __tablename__ = 'plan'
    
    id = Column(PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    basic_monthly_rate=Column(Numeric(10, 2), nullable=False)
    issue_fee=Column(Numeric(10, 2), nullable=False)