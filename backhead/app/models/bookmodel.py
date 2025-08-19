from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func
from sqlalchemy.orm import relationship
from .Base import Base

class Book(Base):
    __tablename__ = 'books'
    BookID = Column(Integer, primary_key=True, autoincrement=True)
    BookName = Column(String(50), nullable=False)
    Author = Column(String(255))
    BookImage = Column(String(2048))
    Category = Column(String(20), nullable=False)
    BookInfo = Column(String(255))
    CreatedTime = Column(TIMESTAMP, server_default=func.now())

    chapters = relationship('Bookchapters', back_populates='books')
