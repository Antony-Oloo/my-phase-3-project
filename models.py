from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    coupons = relationship("Coupon", back_populates="user")

class Coupon(Base):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True)
    code = Column(String, unique=True, nullable=False)
    discount = Column(Integer, nullable=False)
    valid = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="coupons")