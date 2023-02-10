from .base import BaseModel
from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, BOOLEAN

class Admin(BaseModel):
    __tablename__ = 'admin'

    user_id = Column(VARCHAR(), unique=True, nullable=False)

    wallet_admin = Column(VARCHAR(), unique=False, nullable=True)

    currency = Column(VARCHAR(), unique=False, nullable=True)

    price = Column(NUMERIC, unique=False, nullable=True)


class Buyer(BaseModel):
    __tablename__ = 'buyer'

    user_id = Column(VARCHAR(), unique=True, nullable=False)

    name_tg = Column(VARCHAR(32), unique=False, nullable=False)

    wallet_buyer = Column(VARCHAR(), unique=False, nullable=False)


class Good(BaseModel):
    __tablename__ = 'good'

    user_id = Column(VARCHAR(), unique=False, nullable=False)

    name_tg = Column(VARCHAR(), unique=False, nullable=False)

    name_good = Column(VARCHAR(), unique=False, nullable=False)

    quantity = Column(NUMERIC, unique=False, nullable=False)

    currency = Column(VARCHAR(), unique=False, nullable=False)

    rate = Column(NUMERIC, unique=False, nullable=False)

    wallet = Column(VARCHAR(), unique=False, nullable=False)

    status = Column(BOOLEAN, unique=False, nullable=False)


class Seller(BaseModel):
    __tablename__ = 'seller'

    user_id = Column(VARCHAR(), unique=True, nullable=False)

    name_tg = Column(VARCHAR(), unique=False, nullable=False)

    premium = Column(BOOLEAN, unique=False, nullable=False)