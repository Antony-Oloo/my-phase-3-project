from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    coupons = relationship("Coupon", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")  

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    discount_percentage = Column(Integer, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))  
    user = relationship("User", back_populates="coupons")

    transactions = relationship("Transaction", back_populates="coupon")  

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))  
    coupon_id = Column(Integer, ForeignKey('coupons.id'))  
    status = Column(String, nullable=False)  
    transaction_date = Column(DateTime, default=func.now())  

    user = relationship("User", back_populates="transactions")  
    coupon = relationship("Coupon", back_populates="transactions")
