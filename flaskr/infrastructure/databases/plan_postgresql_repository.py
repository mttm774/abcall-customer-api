from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from uuid import UUID
from ...domain.models import Plan
from ...domain.interfaces import PlanRepository
from ...infrastructure.databases.model_sqlalchemy import Base, PlanModelSqlAlchemy

class PlanPostgresqlRepository(PlanRepository):
    def __init__(self, connection_string: str):
        self.engine = create_engine(connection_string)
        self.Session = sessionmaker(bind=self.engine)
        self._create_tables()

    def _create_tables(self):
        Base.metadata.create_all(self.engine)

    
    def get_rate_plan(self,plan_id):
        session = self.Session()
        try:
            print(f'el plan id {plan_id}')
            return session.query(PlanModelSqlAlchemy.basic_monthly_rate).filter(PlanModelSqlAlchemy.id == plan_id).first()
        finally:
            session.close()
