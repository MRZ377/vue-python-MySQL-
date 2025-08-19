from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .Base import Base

class User(Base):
    __tablename__ = 'users'
    UserID = Column(Integer, primary_key=True, autoincrement=True)
    UserName = Column(String(50), nullable=False, unique=True)
    PassWord = Column(String(255), nullable=False)
    Permissions = Column(String(50), Enum('user','admin', name='user_permission_enum'), nullable=False, default='user')
    CreatedTime = Column(TIMESTAMP, server_default=func.now())
