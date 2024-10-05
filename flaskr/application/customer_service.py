from typing import List
from ..domain.models import Customer
import requests
from ..domain.interfaces.customer_repository import CustomerRepository
from ..infrastructure.mappers import CustomerMapper
import uuid
from datetime import datetime
from ..utils import Logger
from  config import Config

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository=None):
        self.log = Logger()
        self.customer_repository=customer_repository

    