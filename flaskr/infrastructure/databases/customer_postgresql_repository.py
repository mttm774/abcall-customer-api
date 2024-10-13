from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from uuid import UUID
from ...domain.models import Customer
from ...domain.interfaces import CustomerRepository
from ...infrastructure.databases.customer_model_sqlalchemy import Base, CustomerModelSqlAlchemy
from ...infrastructure.databases.plan_model_sqlalchemy import PlanModelSqlAlchemy

class CustomerPostgresqlRepository(CustomerRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)


    def get_customer_plan(self,customer_id):
        session = self.Session()
        try:
            result= session.query(PlanModelSqlAlchemy.basic_monthly_rate).join(CustomerModelSqlAlchemy, CustomerModelSqlAlchemy.plan_id == PlanModelSqlAlchemy.id).filter(CustomerModelSqlAlchemy.id == customer_id).first()
            return float(result[0])
        finally:
            session.close()
