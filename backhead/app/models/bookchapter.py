from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship
from .Base import Base

class Bookchapters(Base):
    __tablename__ = 'chapters'

    BookID = Column(Integer, ForeignKey('books.BookID'), primary_key=True)
    ChapterNO = Column(Integer, nullable=False, primary_key=True)
    ChapterTitle = Column(String(255), nullable=False)
    CreatedTime = Column(TIMESTAMP, server_default=func.now())

    books = relationship('Book', back_populates='chapters')
