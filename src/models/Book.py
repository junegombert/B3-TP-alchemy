from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from . import Base

class Book(Base):
  __tablename__ = "books"
  book_id = Column(Integer, primary_key=True)
  book_name = Column(String)
  book_publisher: Mapped[int] = mapped_column(ForeignKey("publishers.publisher_id"))

  def __repr__(self):
    return self.book_name